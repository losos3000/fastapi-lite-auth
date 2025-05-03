from fastapi import FastAPI, APIRouter
import uvicorn

import configurations.config as config
import configurations.api_config as api_config

from api.routers.app import router as app_router


app = FastAPI(
    title=config.PROJECT_NAME,
    version=config.PROJECT_VERSION,
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