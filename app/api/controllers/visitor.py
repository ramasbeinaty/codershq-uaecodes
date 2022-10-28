from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import RedirectResponse

from sqlalchemy.orm import Session

from app.db.base import get_db
from app.core.crud.visitor import add_visitor
from app.core.crud.ambassador import add_points

from app.core.config import settings

router = APIRouter()


@router.get("/{unique_url_key}")
def redirect(unique_url_key, request: Request, db: Session = Depends(get_db)):
        client_ip = request.client.host

        try:
                visitor = add_visitor(db=db, ip_address=client_ip, url_key=unique_url_key)
                ambassador = add_points(db=db, url_key=unique_url_key)
        except Exception as e:
                print("Warning: did not add a new point to ambassador - ", e)

        return RedirectResponse(settings.TARGET_URL)
