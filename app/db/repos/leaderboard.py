from sqlalchemy.orm import Session
from app.db import models

def get_leaderboard_repo(db: Session, skip: int, limit: int):
    leaderboard = db.query(models.Ambassadors).offset(skip).limit(limit).all()
    return leaderboard