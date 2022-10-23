from fastapi import APIRouter

from app.api.controllers import clicks

api_router = APIRouter(prefix="/api")

# root api endpoint
@api_router.get("/")
async def read_root():
        return {"status": "alive"}

api_router.include_router(clicks.router, prefix="/clicks", tags="clicks")