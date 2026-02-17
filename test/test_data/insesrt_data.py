import asyncio
from posixpath import abspath, dirname


from dao import (
    OrganizationDAO,
    DivisionDAO,
    UserDAO,
    ProjectDAO,
    ActivityTypeDAO,
    TaskDAO,
)

from constants import (
    organizations,
    divisions,
    users,
    projects,
    activity_types,
    tasks,
)


async def create_organizations(organizations_: list[dict]):
    """Creates several organizations"""
    new_organizations = await OrganizationDAO.add_many(organizations_)
    return new_organizations


async def create_divisions(divisions_: list[dict]):
    """Creates several divisions"""
    new_divisions = await DivisionDAO.add_many(divisions_)
    return new_divisions


async def create_users(users_: list[dict]):
    """Creates several users"""
    new_users = await UserDAO.add_many(users_)
    return new_users


async def create_projects(projects_: list[dict]):
    """Creates several projects"""
    new_projects = await ProjectDAO.add_many(projects_)
    return new_projects


async def create_activity_types(activity_types_: list[dict]):
    """Creates several activity_types"""
    new_activity_types = await ActivityTypeDAO.add_many(activity_types_)
    return new_activity_types


async def create_tasks(tasks_: list[dict]):
    """Creates several tasks"""
    new_tasks = await TaskDAO.add_many(tasks_)
    return new_tasks


async def main():
    task01 = create_organizations(organizations_=list(organizations))
    task02 = create_divisions(divisions_=list(divisions))
    task03 = create_users(users_=list(users))
    task04 = create_projects(projects_=list(projects))
    task05 = create_activity_types(activity_types_=list(activity_types))
    task06 = create_tasks(tasks_=list(tasks))

    await task01
    await task02
    await task03
    await task04
    await task05
    await task06


if __name__ == "__main__":
    asyncio.run(main())
