from fastapi import APIRouter

from app.api.controllers import ambassador, visitor

api_router = APIRouter()

# root api endpoint
@api_router.get("/")
async def read_root():
        return {"status": "alive"}

api_router.include_router(visitor.router, prefix="/links", tags="links")
api_router.include_router(ambassador.router, prefix="/leaderboard", tags="leaderboard")
