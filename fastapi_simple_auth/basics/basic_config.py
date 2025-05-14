from datetime import datetime
from fastapi_simple_auth.basics.basic_models import BasicUserModel
from fastapi_simple_auth.basics.basic_schemas import BasicLoginSchema, BasicGetUserSchema


# TOKEN CONFIG
SECRET_KEY: str = str(datetime.now().strftime("%Y%m%d%H%M%S"))
TOKEN_LOCATION = ["cookies"]


# COOKIE CONFIG
COOKIE_NAME = "auth_token"
COOKIE_HTTPONLY=False
COOKIE_SECURE=False
COOKIE_SAMESITE="lax"
COOKIE_MAX_AGE=3600
COOKIE_PATH="/"
COOKIE_DOMAIN=None
COOKIE_EXPIRES=None


# LOGIN CONFIG
LOGIN_FIELD_NAME = "username"
PASSWORD_FIELD_NAME = "password"


# MODELS CONFIG
USER_MODEL = BasicUserModel


# SCHEMAS CONFIG
LOGIN_SCHEMA = BasicLoginSchema
GET_USER_SCHEMA = BasicGetUserSchema
