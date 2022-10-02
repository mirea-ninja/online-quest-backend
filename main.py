# import sentry_sdk
from fastapi import FastAPI

from app.config import config
from app.core.server import Server

# sentry_sdk.init(
#     dsn=config.BACKEND_SENTRY_DSN,
#     traces_sample_rate=1.0,
# )
server = Server()
app = server.create_app(
    FastAPI(
        title=config.BACKEND_PROJECT_NAME,
        openapi_url=f"{config.BACKEND_API_V1_PREFIX}/openapi.json",
    )
)
