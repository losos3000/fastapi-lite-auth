import os
from configurations.config import env


env()


SECRET_KEY = os.getenv("AUTH_SECRET_KEY")
TOKEN_LOCATION = ["cookies"]

COOKIE_NAME = "auth_token"
COOKIE_HTTPONLY=False
COOKIE_SECURE=False
COOKIE_SAMESITE="lax"
COOKIE_MAG_AGE=3600
COOKIE_PATH="/"
COOKIE_DOMAIN="localhost"