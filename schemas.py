from pydantic import BaseModel


class BaseRecipe(BaseModel):
    name_recipe: str
    time_cook: int
    description: str


class BookIn(BaseRecipe):
    ingredients: str


class BookOut(BaseRecipe):
    id: int
    count_views: int
    ingredients: str

    class Config:
        orm_mode = True
