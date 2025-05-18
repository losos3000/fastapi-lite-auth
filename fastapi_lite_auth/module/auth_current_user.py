from functools import wraps

from authx.exceptions import AuthXException
from fastapi import HTTPException

from fastapi_lite_auth.module.auth_config import auth_config
from fastapi_lite_auth.module.auth_manager import auth_manager


def auth_exception(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except AuthXException:
            raise HTTPException(
                status_code=401,
                detail={
                    "status": "Unauthorized",
                    "message": "Unauthorized",
                }
            )

        except HTTPException as e:
            print(e)
            raise e

        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=401,
                detail={
                    "status": "Unauthorized",
                    "message": "Unauthorized",
                }
            )
    return wrapper


@auth_config.auth.set_subject_getter
def subject_getter(uid: str) -> auth_config.schemas_config.GetUserSchema | None:
    try:
        user: auth_config.schemas_config.GetUserSchema = auth_manager.get_current_user(uid)
        return user
    except Exception as e:
        print(e)
        raise HTTPException(
                status_code=401,
                detail={
                    "status": "Unauthorized",
                    "message": "Wrong token",
                }
            )


current_user = auth_exception(auth_config.auth.get_current_subject)