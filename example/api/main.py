import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from example.api.routers.user import router as user_router
from example.api.routers.auth import router as auth_router
from example.database.database import create_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Example start")
    create_db()
    yield
    print("Example Stop")


app = FastAPI(
    title="Authentication Module Example",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    router=auth_router,
    prefix="/api",
    tags=["AUTH"]
)

app.include_router(
    router=user_router,
    prefix="/api",
    tags=["USERS"]
)


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
    )