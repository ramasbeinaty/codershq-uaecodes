from os import link
import string
from turtle import update
from sqlalchemy.orm import Session
from app.db import models

from app.db.base import settings

def get_ambassadors_repo(db: Session, skip: int, limit: int):
    ambassadors = db.query(models.Ambassadors).order_by(models.Ambassadors.points.desc()).offset(skip).limit(limit).all() 
    return ambassadors

def add_points_repo(db: Session, url_key: string):
    ambassador = db.query(models.Ambassadors).filter(models.Ambassadors.link==url_key).first()
    
    if ambassador is None:
        print("INFO: no ambassador found with given url")
        return None

    ambassador.points += 1

    # db.query(models.Ambassadors).filter(models.Ambassadors.link==server_url).update({"points": models.Ambassadors.points+=1})

    db.add(ambassador)
    db.commit()
    db.refresh(ambassador)

    return ambassador