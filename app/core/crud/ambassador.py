import string
from sqlalchemy.orm import Session

from app.db.repos.ambassador import get_ambassadors_repo, add_points_repo

def get_ambassadors(db: Session, skip: int, limit: int):
    ambassador = None
    try:
        ambassador = get_ambassadors_repo(db=db, skip=skip, limit=limit)
        print("INFO: Successfully retrieved ambassadors")
    except Exception as e:
        print("ERROR: Failed to retrieve ambassadors - ", e)

    return ambassador

def add_points(db: Session, url_key: string):
    ambassador = None

    try:
        ambassador = add_points_repo(db=db, url_key=url_key)
        print("INFO: Successfully added points to ambassador")
    except Exception as e:
        raise ValueError("ERROR: Failed to add points to ambassador - ", e)

    return ambassador