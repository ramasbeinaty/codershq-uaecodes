from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import RedirectResponse

from sqlalchemy.orm import Session

from app.db.base import get_db
from app.core.crud.visitor import add_visitor
from app.core.crud.ambassador import add_points

router = APIRouter()


@router.get("/")
def redirect(request: Request, db: Session = Depends(get_db)):
        client_ip = request.client.host
        server_url = request.url

        try:
                visitor = add_visitor(db=db, ip_address=client_ip, server_url=server_url)
                points = add_points(db=db, server_url=server_url)
        except Exception as e:
                print("Warning: failed to add points to ambassador - ", e)

        return RedirectResponse("https://ai.gov.ae/uaecodes/")
