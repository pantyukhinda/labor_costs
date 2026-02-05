import asyncio
from posixpath import abspath, dirname
import random
import sys
from httpx import ASGITransport, AsyncClient


sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))) + "/app")

from app.main import app


async def async_client_post(url: str, json: dict):
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
    await async_client_post(
        url=url,
        json=json,
    )


async def create_test_division(
    url: str = "division/add",
):
    """Create a test division"""
    json = {
        "division": {
            "level_01": "lev_01",
            "level_02": "lev_02",
            "level_03": "lev_03",
            "level_04": "lev_04",
        },
        "organization_id": f"{random.randint(1, 10)}",
    }
    await async_client_post(
        url=url,
        json=json,
    )


# TODO: Add method to create a user
# async def create_test_user(
#     url: str = "user/add",
# ):
#     """Create a test user"""
#     json = ({},)

#     async with AsyncClient(
#         transport=ASGITransport(app=app),
#         base_url="http://",
#     ) as async_client:
#         await async_client.post(url=url, json=json)


# Insert into Users

# Insert into Projects

# Insert into ActivityTypes

# Insert into Tasks

if __name__ == "__main__":

    from constants import ORGANIZATION_NAMES

    async def main():
        for organization in ORGANIZATION_NAMES:
            await create_test_organization(
                organization_name=organization,
            )

        for _ in range(20):
            await create_test_division()

    asyncio.run(main())
