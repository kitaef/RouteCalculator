from sqlalchemy import Column, Integer, JSON

from db.base_class import Base


class Route(Base):
    id = Column(Integer, primary_key=True)
    points = Column(JSON)