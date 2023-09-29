from fastapi import APIRouter, status
from schema import schemas
from api import ai_model

router = APIRouter(tags=["AI-Model"], prefix="/model")

@router.post("/predict", status_code=status.HTTP_200_OK, response_model=schemas.PredictResp)
async def predict(request: schemas.PredictReq):
    return ai_model.query_model(request)