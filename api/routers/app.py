from fastapi import APIRouter

from api.routers.auth import router as auth_router
from api.routers.user import router as user_router


router = APIRouter()


router.include_router(
    router=auth_router,
    tags=["AUTH"],
)

router.include_router(
    router=user_router,
    tags=["USERS"],
)


@router.get(
    path="/status",
    tags=["DEFAULT"],
)
async def get_api_status():
    '''
    Status router
    '''
    return {"status": "OK"}

