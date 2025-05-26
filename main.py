from contextlib import asynccontextmanager
from typing import List

from fastapi import FastAPI, HTTPException
from sqlalchemy.future import select

from database import engine, session
from models import Recipe
from schemas import BookIn, BookOut


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Recipe.metadata.create_all)
    yield
    await session.close()
    await engine.dispose()


app = FastAPI(lifespan=lifespan)


@app.post("/recipes/", response_model=BookOut)
async def create_recipe(book: BookIn) -> Recipe:
    new_recipe = Recipe(**book.model_dump())
    async with session.begin():
        session.add(new_recipe)
    await session.commit()
    return new_recipe


@app.get("/recipes/", response_model=List[BookOut])
async def get_recipes():
    res = await session.execute(
        select(Recipe).order_by(Recipe.count_views.desc(), Recipe.time_cook)
    )
    return res.scalars().all()


@app.get("/recipes/{recipe_id}", response_model=BookOut)
async def get_recipe_by_id(recipe_id: int) -> Recipe:
    async with session as async_session:
        res = await async_session.get(Recipe, recipe_id)
        if res is None:
            raise HTTPException(status_code=404, detail="Рецепт не найден")
        res.count_views += 1
        await session.commit()
        return res
