import asyncio
from posixpath import abspath, dirname
import random
import sys
from httpx import ASGITransport, AsyncClient
from faker import Faker


sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))) + "/app")

from constants import ORGANIZATION_NAMES
from constants import FIRST_NAMES
from constants import LAST_NAMES
from constants import PATRONYMICS

# from database import connection
from app.main import app

# NUMBER_OF_ORGANIZATIONS = 10
NUMBER_OF_DIVISIONS = 10
NUMBER_OF_USERS = 100

fake = Faker()


async def _async_client_post(url: str, json: dict):
    """Executes the post method by an asynchronous client"""
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://",
    ) as async_client:
        await async_client.post(url=url, json=json)


async def create_test_organization(
    organization_name: str,
    url: str = "organizations/add",
):
    """Create a test organization"""
    json = {
        "name": organization_name,
    }
    await _async_client_post(
        url=url,
        json=json,
    )


# TODO: Add autogenerate divisions.
async def create_test_division(
    url: str = "division/add",
):
    """Create a test division"""
    json = {
        "division": {
            "level_01": "Directorate",
            "level_02": "Department",
            "level_03": "Sector",
            "level_04": "Group",
        },
        "organization_id": f"{random.randint(1, 10)}",
    }
    await _async_client_post(
        url=url,
        json=json,
    )


async def create_test_user(
    last_name: str,
    first_name: str,
    patronymic: str,
    email: str,
    password: str,
    division_id: int,
    url: str = "user/add",
):
    """Create a test user"""
    json = {
        "last_name": last_name,
        "first_name": first_name,
        "patronymic": patronymic,
        "email": email,
        "password": password,
        "division_id": division_id,
    }

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://",
    ) as async_client:
        await async_client.post(url=url, json=json)

    # Insert into Projects

    # Insert into ActivityTypes

    # Insert into Tasks


async def add_organizations():
    """Create organizations in the database"""
    for organization in ORGANIZATION_NAMES:
        await create_test_organization(
            organization_name=organization,
        )


async def add_divisions():
    """Create divisions in the database"""
    for _ in range(NUMBER_OF_DIVISIONS):
        await create_test_division()


async def add_users():
    """Create users in the database"""
    for _ in range(NUMBER_OF_USERS):
        await create_test_user(
            last_name=random.choice(LAST_NAMES),
            first_name=random.choice(FIRST_NAMES),
            patronymic=random.choice(PATRONYMICS),
            email=fake.email(),
            password="123456",
            division_id=random.randint(1, NUMBER_OF_DIVISIONS),
        )


async def main():
    tasks = [
        add_organizations(),
        add_divisions(),
        add_users(),
    ]
    await asyncio.gather(*tasks)


if __name__ == "__main__":

    asyncio.run(main())
