from fastapi import HTTPException

from authentication.module.auth_config import auth_config


class AuthManager:
    def __init__(self):
        pass


    def model_validate(
            self,
            user_model: auth_config.models_config.UserModel
    ) -> auth_config.schemas_config.GetUserSchema:
        return auth_config.schemas_config.GetUserSchema.model_validate(user_model, from_attributes=True)


    # TODO Сделать хеширование
    def hash(self, data: str) -> str:
        return data


    def get_user(self, login: str) -> auth_config.models_config.UserModel | None:
        raise ValueError('''Необходимо переопределить метод get_user для auth_manager.
Пример:
---

from fastapi import APIRouter
from authentication import auth_router, auth_config, auth_manager

def get_user(login: str) -> auth_config.models_config.UserModel | None:
    ...
    return user

auth_manager.get_user = get_user

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

        # TODO Сделать универсальное преобразование
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
            # TODO Сделать универсальное преобразование
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
