
from app.db.base import Base

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.dialects.postgresql import INET

from app.db.base import settings

class Ambassadors(Base):
    __tablename__ = settings.AMBASSADORS_TABLE

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    link = Column(String, unique=True, index=True, nullable=True)
    points = Column(Integer, nullable=False, default=0)
    is_valid = Column(Boolean, nullable=False, default=False)

class Visitor(Base):
    __tablename__ = settings.VISITORS_TABLE

    id = Column(Integer, unique=True, nullable=False)
    ip_address = Column(INET, primary_key=True, index=True)
    url = Column(String, primary_key=True, index=True)

