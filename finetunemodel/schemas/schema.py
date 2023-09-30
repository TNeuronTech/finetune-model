from pydantic import BaseModel

class PredictReq(BaseModel):
    prompt: str
    key: str

class PredictResp(BaseModel):
    result: str


class TrainResp(BaseModel):
    key: str