
from finetunemodel.schemas import schema

from finetunemodel.models.model import ai_model


def query_model(request: schema.PredictReq):
    return {"result": ai_model.get_query_results(request.prompt, request.key)}


def train_model(uploaded_file):
    return {"key": ai_model.train_and_get_key(uploaded_file)}