from langchain.llms import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFLoader
import uuid
from tempfile import NamedTemporaryFile

from finetunemodel.config.settings import settings

class Model:
    def __init__(self) -> None:
        self.textSplitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=0)
        self.embeddings = OpenAIEmbeddings()
        pass

    def get_query_results(self, prompt, key) -> str:
        index = Chroma(persist_directory=f"{settings.DB_LOCATION}/{key}", embedding_function=self.embeddings)
        self.retrieval = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=index.as_retriever())
        return self.retrieval.run(prompt)

    def train_and_get_key(self, uploaded_file) -> str:
        
        with NamedTemporaryFile(delete=True) as temp_file:
            temp_file.write(uploaded_file.file.read())
            temp_file_path = temp_file.name
            loader = PyPDFLoader(temp_file_path)
            data = loader.load() 
          
        
        texts = self.textSplitter.split_documents(data)
        key = str(uuid.uuid1())
        index = Chroma.from_documents(texts, self.embeddings, persist_directory=f"{settings.DB_LOCATION}/{key}")
        index.persist()
        return key
    
ai_model = Model()


