from fastapi import APIRouter

from app.api.controllers import leaderboard, links

api_router = APIRouter(prefix="/api")

# root api endpoint
@api_router.get("/")
async def read_root():
        return {"status": "alive"}

api_router.include_router(links.router, prefix="/links", tags="links")
api_router.include_router(leaderboard.router, prefix="/leaderboard", tags="leaderboard")
