from pydantic import BaseModel, EmailStr


class ReadLeaderboard(BaseModel):
    name: str
    email: EmailStr
    points: int

    class Config():
        orm_mode = True
