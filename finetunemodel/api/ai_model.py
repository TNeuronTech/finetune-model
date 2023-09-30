
from finetunemodel.schema import schemas

from finetunemodel.ai_models.model import ai_model


def query_model(request: schemas.PredictReq):
    return {"result": ai_model.get_query_results(request.prompt)}