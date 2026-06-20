from fastapi import FastAPI

from app.api.routes import health, root
from app.core.config import settings


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.add_api_route("/", root, methods=["GET"])
app.add_api_route("/health", health, methods=["GET"])
