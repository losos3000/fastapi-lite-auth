import os
from configurations.config import env


env()


SECRET_KEY = os.getenv("AUTH_SECRET_KEY")
TOKEN_LOCATION = ["cookies"]

COOKIE_NAME = "auth_token"