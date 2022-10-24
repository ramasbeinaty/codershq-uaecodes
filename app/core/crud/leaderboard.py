from sqlalchemy.orm import Session

from app.db.repos.leaderboard import get_leaderboard_repo

def get_leaderboard(db:Session, skip: int, limit: int):
    return get_leaderboard_repo(db=db, skip=skip, limit=limit)