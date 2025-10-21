from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from src.routes import health_router
from src.services import APIServices

logger = logging.getLogger(__name__)

def create_app() -> FastAPI:

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        logger.info("Starting API Services")
        try:
            app.state.services = await APIServices.create("resources/application.conf")
            logger.info("Services Initialized")
        except Exception as e: 
            logger.error("Could not initialize Services")
            raise
        yield
    return FastAPI(lifespan =lifespan)

app = create_app()


app.add_middleware(
    CORSMiddleware, 
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://192.168.2.116:3000",
    ],
    allow_credentials = True,
    allow_methods = ["GET"],
    allow_headers = ["*"],
)

app.include_router(health_router)