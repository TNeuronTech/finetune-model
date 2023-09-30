from pydantic import BaseModel


class PredictReq(BaseModel):
    prompt: str

class PredictResp(BaseModel):
    result: str