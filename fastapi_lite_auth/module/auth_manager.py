from fastapi import HTTPException

from fastapi_lite_auth.module.auth_config import auth_config


class AuthManager:
    def __init__(self):
        pass


    def model_validate(
            self,
            user_model: auth_config.models_config.UserModel
    ) -> auth_config.schemas_config.GetUserSchema:
        return auth_config.schemas_config.GetUserSchema.model_validate(user_model, from_attributes=True)


    def hash(self, data: str) -> str:
        return data


    def get_user(self, login: str) -> auth_config.models_config.UserModel | None:
        raise ValueError('''It is necessary to override the "get_user" method for "auth_manager".
Example:
---

from fastapi import APIRouter
from fastapi_lite_auth import auth_router, auth_config, auth_manager

def get_user_by_login(login: str) -> auth_config.models_config.UserModel | None:
    # Request to Database. Find user by login field.
    return user

auth_manager.get_user = get_user_by_login

app = FastAPI()
app.include_router(router=auth_router)

---''')
        return None


    def get_current_user(self, login: str | None) -> auth_config.schemas_config.LoginSchema | None:
        if login is None:
            raise HTTPException(
                status_code=401,
                detail={
                    "status": "Unauthorized",
                    "message": "Wrong password",
                }
            )
        user_model: auth_config.models_config.UserModel = self.get_user(login=login)

        user = self.model_validate(user_model)
        return user


    def auth_check(
        self,
        data: auth_config.schemas_config.LoginSchema,
    ) -> auth_config.schemas_config.GetUserSchema | None:
        user_model: auth_config.models_config.UserModel = self.get_user(login=data.login)

        if user_model is None:
            raise HTTPException(
                status_code=401,
                detail={
                    "status": "Unauthorized",
                    "message": "Wrong login or password",
                }
            )

        if str(user_model.__dict__[auth_config.login_config.password_field_name]) == self.hash(data.password):
            user = self.model_validate(user_model)
            return user

        raise HTTPException(
            status_code=401,
            detail={
                "status": "Unauthorized",
                "message": "Wrong password",
            }
        )


auth_manager = AuthManager()
