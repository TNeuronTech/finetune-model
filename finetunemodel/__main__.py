import uvicorn
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from finetunemodel.router import ai_model
import os


# add end points
# package and deploy BE to server and query from internet
# how to optimize the results



app = FastAPI(
    title="FineTune",
    description="APIs for FineTune model",
    version="1.0.0",
)

app.include_router(ai_model.router)

if __name__ == "__main__":  
     uvicorn.run(app, host="0.0.0.0", port=8000)