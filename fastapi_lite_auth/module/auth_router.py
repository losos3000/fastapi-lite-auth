from fastapi import APIRouter, HTTPException, Response

from fastapi_lite_auth.module.auth_config import auth_config
from fastapi_lite_auth.module.auth_manager import auth_manager


router = APIRouter()


@router.post(path="/login")
async def login(response: Response, data: auth_config.schemas_config.LoginSchema):
    '''
    Authentication router
    '''
    try:
        user: auth_config.schemas_config.GetUserSchema = auth_manager.auth_check(data)

        token = auth_config.auth.create_access_token(uid=str(user.__dict__[auth_config.login_config.login_field_name]))
        response.set_cookie(
            value=token,
            key=auth_config.cookie_config.cookie_name,
            httponly=auth_config.cookie_config.cookie_httponly,
            secure=auth_config.cookie_config.cookie_secure,
            samesite=auth_config.cookie_config.cookie_samesite,
            max_age=auth_config.cookie_config.cookie_max_age,
            path=auth_config.cookie_config.cookie_path,
            domain=auth_config.cookie_config.cookie_domain,
            expires=auth_config.cookie_config.cookie_expires,
        )
        return {
            "status": "Success",
            "access_token": token
        }

    except HTTPException as e:
        print(e)
        raise e

    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail={
                "status": "Error",
                "message": "Internal Server Error",
            }
        )


@router.get(path="/logout")
async def logout(response: Response):
    '''
    Log out router
    '''
    response.delete_cookie(auth_config.cookie_config.cookie_name)
    return {"status": "Success"}