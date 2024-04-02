from pydantic import BaseModel


class Route(BaseModel):
    id: int
    points: list[dict]

    class Config:
        orm_mode=True