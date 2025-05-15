from fastapi import APIRouter
from hashlib import sha256

from fastapi_simple_auth import auth_config, auth_router, auth_manager

from example.database.scripts import get_user_by_login
from example.database.models import CustomUserModel
from example.api.schemas.user import CustomGetUserSchema


def hash(data: str) -> str:
    return sha256(data.encode()).hexdigest()


auth_config.models_config.UserModel = CustomUserModel
auth_config.schemas_config.GetUserSchema = CustomGetUserSchema

auth_config.token_config.secret_key = "qwerty123"

auth_config.login_config.login_field_name = "email"
auth_config.login_config.password_field_name = "password"

auth_manager.hash = hash
auth_manager.get_user = get_user_by_login

auth_config.authx_ready()

router = APIRouter()
router.include_router(
    router=auth_router
)
