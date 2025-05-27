from pydantic import BaseModel, ConfigDict


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

    model_config = ConfigDict(from_attributes=True)
