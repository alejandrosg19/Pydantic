from fastapi import APIRouter
from serializers.serializers import MetaSerializer

router = APIRouter()


@router.get(
    "/",
    tags=["Meta"],
    response_model=MetaSerializer)
def root():
    """
    Root of host
    """
    output = {
        'message': 'FastAPI API'
    }
    return output


@router.get(
    "/health",
    tags=["Meta"],
    response_model=MetaSerializer)
def health_check():
    """
    Check health of service
    """
    output = {
        "message": "Status OK",
    }
    return output
