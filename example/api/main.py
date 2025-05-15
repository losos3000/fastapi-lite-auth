import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from example.api.routers.user import router as user_router
from example.api.routers.auth import router as auth_router
from example.database.database import create_db

from fastapi_simple_auth import auth_config


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Example start")
    create_db()
    yield
    print("Example Stop")


app = FastAPI(
    title="Authentication Module Example",
    version="1.0.0-rc1",
    description=f'''Example for <a href="https://github.com/losos3000/fastapi-simple-auth/">FastAPI Simple Auth</a>.<br/>
    Module connected in file example/api/routers/auth.py<br/>
    
    Auth fields:
    
    - login: {auth_config.login_config.login_field_name}
    - password: {auth_config.login_config.password_field_name}
    
    ---
    
    Example users:
    
    1. Administrator:
    - full_name: Administrator
    - email: admin@example.com
    - username: admin
    - phone: 000-00-00
    - password: admin
    - passport_number: 000000
    - insurance_number: 000-000
    
    2. User:
    - full_name: User
    - email: user@example.com
    - username: user
    - phone: 123-45-67
    - password: user
    - passport_number: 111222
    - insurance_number: 123-321''',
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