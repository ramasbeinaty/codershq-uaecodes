from fastapi import APIRouter, Depends, status, Request, Header
from fastapi.responses import RedirectResponse
from typing import List, Optional

from app.core.config import settings

from sqlalchemy.orm import Session
from app.core.crud.leaderboard import get_leaderboard

from app.db.base import get_db
from app.schemas import ReadLeaderboard

router = APIRouter()

from fastapi.templating import Jinja2Templates

# get the templates
templates = Jinja2Templates(directory=settings.TEMPLATES_DIR)

@router.get("/", response_model= List[ReadLeaderboard], status_code=status.HTTP_200_OK)
async def read_leaderboard(request: Request, hx_request: Optional[str] = Header(None), db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
        leaderboard = get_leaderboard(db=db, skip=skip, limit=limit)

        context = {"request": request, 'ambassadors': leaderboard}
        if hx_request:
                return templates.TemplateResponse("partials/table.html", context)

        return templates.TemplateResponse("leaderboard.html", context)