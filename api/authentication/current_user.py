from functools import wraps

from authx.exceptions import AuthXException
from fastapi import HTTPException

from api.authentication.auth import auth
from api.schemas.user import UserSchema
from database.scripts.user import get_user


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
                    "message": "Wrong login or password",
                }
            )

        except HTTPException as e:
            raise e

        except Exception:
            raise HTTPException(
                status_code=401,
                detail={
                    "status": "Unauthorized",
                    "message": "Wrong login or password",
                }
            )
    return wrapper



@auth.set_subject_getter
def get_user_from_uid(uid: str) -> UserSchema:
    user: UserSchema = get_user(int(uid))
    return user


current_user = auth_exception(auth.get_current_subject)