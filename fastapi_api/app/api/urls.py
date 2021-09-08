from fastapi import APIRouter
from .meta import views as meta
from .v1 import views as api_v1

urls = APIRouter()

urls.include_router(
    meta.router,
    prefix=""
)

urls.include_router(
    api_v1.router,
    prefix="/api"
)
