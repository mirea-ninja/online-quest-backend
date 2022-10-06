from typing import TypeVar

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from app.config import config
from app.internal.deps import Application

FastAPIInstance = TypeVar("FastAPIInstance", bound="FastAPI")


class Server:
    application = Application

    def __init__(self) -> None:
        self.application = Application()
        self.application.wire(packages=["app.internal.delivery.routes"])

    def create_app(self, app: FastAPIInstance) -> FastAPI:
        app.container = self.application

        # Set all CORS enabled origins
        if config.BACKEND_CORS_ORIGINS:
            app.add_middleware(
                CORSMiddleware,
                allow_origins=[str(origin) for origin in config.BACKEND_CORS_ORIGINS],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )

        app.mount("/static", StaticFiles(directory="./app/tasks/static"), name="static")
        self._register_routes(app)
        self._register_controllers()
        return app

    @staticmethod
    def _register_routes(app: FastAPIInstance) -> None:
        from app.internal.delivery.routes import __router__

        app.include_router(__router__)

    def _register_controllers(self) -> None:
        pass
