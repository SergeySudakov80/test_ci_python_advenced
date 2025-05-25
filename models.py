from sqlalchemy import Column, String, Integer

from database import Base


class Recipe(Base):
    __tablename__ = 'recipe'
    id = Column(Integer, primary_key=True, index=True)
    name_recipe = Column(String, index=True)
    count_views = Column(Integer, index=True, default=0)
    time_cook = Column(Integer)
    description = Column(String)
    ingredients = Column(String)
