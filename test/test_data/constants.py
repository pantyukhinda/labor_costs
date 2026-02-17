"""These datasets are designed to insert rows into each table."""

from datetime import date, datetime
import random
from typing import Any, Generator
from faker import Faker

# It uses:
# >> rows for Organizations
N_ORG = 10

# >> rows for ActivityTypes
N_ACT_TYPES = 10

# >> division records for each Organization
N_DIV = 10

# >> project records for each Organization
N_PROJ = 10

# >> user records for each Organization
N_USER = 100

# >> task records for each User
N_TASK = 100


faker = Faker(locale="ru_RU")


ACTIVITY_TYPES = [
    "Аналитика",
    "Разработка",
    "Тестирование",
    "Деплой",
    "Совещание",
    "Обучение",
    "Поддержка",
    "Документация",
    "Мониторинг",
    "Ревью кода",
]


def generate_organization(n_org: int = N_ORG) -> Generator:
    """Organization generator"""
    while n_org > 0:
        organization = {
            "name": faker.company(),
        }
        n_org -= 1

        yield organization


# TODO: Create 10 division records for every organization
def generate_division(
    n_division: int = N_DIV,
) -> Generator:
    """Division generator"""
    while n_division >= 0:
        division = {
            "division": {
                "level_01": "Directorate",
                "level_02": "Department",
                "level_03": "Sector",
                "level_04": faker.job_male(),
            },
            "organization_id": random.randint(1, N_ORG),
        }

        n_division -= 1

        yield division


def generate_user(
    n_user: int = N_USER,
) -> Generator:
    """User generator"""
    while n_user >= 0:
        user = {
            "last_name": faker.last_name_male(),
            "first_name": faker.first_name_male(),
            "patronymic": faker.middle_name_male(),
            "email": faker.email(),
            "password": "qwe",
            "division_id": random.randint(1, N_DIV),
        }
        n_user -= 1

        yield user


# Create 10 project records for every organization
def generate_project(
    n_project: int = N_PROJ,
) -> Generator:
    """Project generator"""
    while n_project >= 0:
        project = {
            # "name": random.choice(PROJECT_NAMES),
            "name": faker.bs(),
            "completed": False,
            "organization_id": random.randint(1, N_ORG),
        }

        n_project -= 1

        yield project


def generate_activity_type(
    n_activity_type: int = N_ACT_TYPES,
) -> Generator:
    """Activity type generator"""
    while n_activity_type >= 0:
        activity_type = {
            "name": random.choice(ACTIVITY_TYPES),
            "organization_id": random.randint(1, N_ORG),
            "visible": True,
        }

        n_activity_type -= 1

        yield activity_type


# Use all divisions and all projects
def generate_task(
    n_task: int = N_TASK,
) -> Generator:
    """Task generator"""
    while n_task >= 0:
        task = {
            "user_id": random.randint(1, N_USER),
            "project_id": random.randint(1, N_PROJ),
            "type_of_activity_id": random.randint(1, N_ACT_TYPES),
            "start_time": datetime.combine(
                faker.date_between_dates(
                    date_start=date(year=2025, month=1, day=1),
                    date_end=date(year=2025, month=7, day=1),
                ),
                datetime.min.time(),
            ),
            "end_time": datetime.combine(
                faker.date_between_dates(
                    date_start=date(year=2025, month=7, day=1),
                    date_end=date(year=2025, month=12, day=31),
                ),
                datetime.min.time(),
            ),
            "description": faker.sentence(nb_words=10),
        }

        n_task -= 1

        yield task


organizations = generate_organization()
divisions = generate_division()
users = generate_user()
projects = generate_project()
activity_types = generate_activity_type()
tasks = generate_task()

# TODO: Дописать скрипт для назначения реальных id
