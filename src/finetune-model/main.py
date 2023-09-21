from model.model import Model
from dotenv import load_dotenv
load_dotenv()


model = Model()

print(model.get_query_results("Summarize this content in 5 points"))