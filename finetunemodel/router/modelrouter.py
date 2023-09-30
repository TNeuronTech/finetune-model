from fastapi import APIRouter, status, File, UploadFile
from finetunemodel.schemas import schema
from finetunemodel.api import api

router = APIRouter(tags=["AI-Model"], prefix="/model")

@router.post("/predict", status_code=status.HTTP_200_OK, response_model=schema.PredictResp)
async def predict(request: schema.PredictReq):
    return api.query_model(request)



@router.post("/train", status_code=status.HTTP_201_CREATED, response_model=schema.TrainResp)
async def train(file: UploadFile):
    return api.train_model(file)