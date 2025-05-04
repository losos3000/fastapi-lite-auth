from fastapi import APIRouter, HTTPException, Response

from api.schemas.auth import LoginSchema

from api.authentication.auth import auth, config
from configurations.auth_config import (
    COOKIE_HTTPONLY,
    COOKIE_SAMESITE,
    COOKIE_PATH,
    COOKIE_SECURE,
    COOKIE_MAG_AGE,
    COOKIE_DOMAIN,
)
from database.scripts.user import get_user_id


router = APIRouter()


@router.post(path="/login")
async def login(data: LoginSchema, response: Response):
    '''
    Authentication router
    '''
    try:
        user_id = await get_user_id(data.username)

        if user_id is None:
            raise HTTPException(
                status_code=401,
                detail={
                    "status": "Unauthorized",
                    "message": "Wrong login or password",
                }
            )

        token = auth.create_access_token(uid=f"{user_id}")
        response.set_cookie(
            key=config.JWT_ACCESS_COOKIE_NAME,
            value=token,
            httponly=COOKIE_HTTPONLY,
            # secure=COOKIE_SECURE,
            samesite=COOKIE_SAMESITE,
            max_age=COOKIE_MAG_AGE,
            path=COOKIE_PATH,
            # domain=COOKIE_DOMAIN,
        )
        return {"access_token": token}

    except HTTPException as e:
        raise e

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "status": "Error",
                "message": "Internal Server Error :(",
            }
        )


@router.get(
    path="/logout",
)
async def logout(
    response: Response,
):
    '''
    Log out router
    '''
    response.delete_cookie(auth.config.JWT_ACCESS_COOKIE_NAME)
    return {"logout": "OK"}