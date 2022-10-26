import string
from sqlalchemy.orm import Session

from app.db.repos.ambassador import get_ambassadors_repo, add_points_repo

def get_ambassadors(db: Session, skip: int, limit: int):
    ambassador = None
    try:
        ambassador = get_ambassadors_repo(db=db, skip=skip, limit=limit)
    except Exception as e:
        raise Exception("ERROR: Failed to add ambassador. Ambassador already exists - ", e)

    return ambassador

def add_points(db: Session, server_url: string):
    points = 0

    try:
        points = add_points_repo(db=db, server_url=server_url)
    except Exception as e:
        raise Exception("ERROR: Failed to add points to ambassador - ", e)

    return points