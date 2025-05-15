from fastapi import APIRouter, HTTPException, Depends

from fastapi_simple_auth import current_user


router = APIRouter()


@router.get(path="/users")
async def get_user(user = Depends(current_user)):
    try:
        return {"user": user}

    except HTTPException as e:
        raise e

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "status": "Error",
                "message": "Internal Server Error",
            },
        )