from fastapi import APIRouter
from api.schemas.models import PredictRequest, PredictResponse
from api.services.hf_client import predict

router = APIRouter(prefix="/v1", tags=["prediction"])


@router.post("/predict", response_model=PredictResponse)
async def predict_text(req: PredictRequest):
    result = await predict(req.text)

    if "error" in result:
        return PredictResponse(label="error", score=0.0)

    # HF returns list like [{'label': 'hate', 'score': 0.59}]
    first = result[0] if isinstance(result, list) else result
    return PredictResponse(label=first["label"], score=float(first["score"]))
