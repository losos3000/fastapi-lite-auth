from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

import configurations.config as config
import configurations.api_config as api_config

from api.routers.app import router as app_router


app = FastAPI(
    title=config.PROJECT_NAME,
    version=config.PROJECT_VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=api_config.CORS_ORIGINS,
    allow_credentials=api_config.CORS_CREDENTIALS,
    allow_methods=api_config.CORS_METHODS,
    allow_headers=api_config.CORS_HEADERS,
)


app.include_router(
    router=app_router,
    prefix="/api",
)


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=api_config.API_HOST,
        port=api_config.API_PORT,
    )