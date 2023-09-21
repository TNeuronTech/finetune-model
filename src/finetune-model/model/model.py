from langchain.llms import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA

from config.settings import settings

class Model:
    def __init__(self) -> None:
        # print(settings.LLM_NAME)
        self.textSplitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=0)
        self.embeddings = OpenAIEmbeddings()
        
        index = Chroma(persist_directory=settings.DB_LOCATION, embedding_function=self.embeddings)
        self.retrieval = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=index.as_retriever())

        pass

    def get_query_results(self, prompt) -> str:
        return self.retrieval.run(prompt)




