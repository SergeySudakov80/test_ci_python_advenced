import pytest
from httpx import ASGITransport, AsyncClient

from main import app


@pytest.mark.anyio
async def test_post_recipes():
    new_recipe = {
        "name_recipe": "test",
        "time_cook": 0,
        "description": "string",
        "count_views": 0,
        "ingredients": "string",
    }
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        responce = await ac.post("/recipes/", json=new_recipe)
    assert responce.status_code == 200


@pytest.mark.anyio
async def test_get_recipe():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        responce = await ac.get("/recipes/")
    assert responce.status_code == 200
    assert responce.json()[0]["name_recipe"] == "test"
