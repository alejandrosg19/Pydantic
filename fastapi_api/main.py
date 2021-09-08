from fastapi import FastAPI
from .app.api.urls import urls

app = FastAPI(
    title="FastAPI Docs",
    redoc_url="/docs/redoc",
    docs_url='/docs/swagger',
)

app.include_router(urls)
