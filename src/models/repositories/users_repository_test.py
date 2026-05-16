import pytest
from .users_repository import UsersRepository


@pytest.mark.asyncio
async def test_insert_users():
    new_user = {
        "user_name": "Fulano",
        "age": 30,
        "uf": "SP"
    }
    repo = UsersRepository()
    await repo.insert_users(new_user)


@pytest.mark.asyncio
async def test_get_users_by_name():
    repo = UsersRepository()
    response = await repo.get_users_by_name("Fulano")

    assert isinstance(response, list)
    assert len(response) > 0
    assert response[0]["user_name"] == "Fulano"
