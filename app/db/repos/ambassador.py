from os import link
import string
from turtle import update
from sqlalchemy.orm import Session
from app.db import models

from app.db.base import settings

def get_ambassadors_repo(db: Session, skip: int, limit: int):
    leaderboard = db.query(models.Ambassadors).offset(skip).limit(limit).all() 
    return leaderboard

def add_points_repo(db: Session, server_url: string):
    ambassador = models.Ambassadors(
        db.query(models.Ambassadors).filter(models.Ambassadors.link==server_url).first()
        )

    ambassador.points += 1

    # db.query(models.Ambassadors).filter(models.Ambassadors.link==server_url).update({"points": models.Ambassadors.points+=1})

    db.add(ambassador)
    db.commit()
    db.refresh(ambassador)

    return ambassador