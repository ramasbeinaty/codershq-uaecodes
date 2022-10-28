from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from app.api.controllers import ambassador, visitor

from app.core.config import settings

api_router = APIRouter()

# root api endpoint
@api_router.get("/")
async def read_root():
        return RedirectResponse(settings.TARGET_URL)

api_router.include_router(visitor.router, prefix="/links", tags="links")
api_router.include_router(ambassador.router, prefix="/leaderboard", tags="leaderboard")
