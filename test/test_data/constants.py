"""These datasets are designed to insert 10 rows into each table"""

from datetime import datetime
import random
from faker import Faker

faker = Faker()


FIRST_NAMES = [
    "Иван",
    "Сергей",
    "Дмитрий",
    "Алексей",
    "Виктор",
    "Артем",
    "Максим",
    "Роман",
    "Станислав",
    "Егор",
]

LAST_NAMES = [
    "Иванов",
    "Петров",
    "Сидоров",
    "Кузнецов",
    "Смирнов",
    "Орлов",
    "Федоров",
    "Волков",
    "Морозов",
    "Зайцев",
]


PATRONYMICS = [
    "Иванович",
    "Сергеевич",
    "Дмитриевич",
    "Алексеевич",
    "Викторович",
    "Артемович",
    "Максимович",
    "Романович",
    "Станиславович",
    "Егорович",
]

ORGANIZATION_NAMES = [
    "ТехноСфера",
    "Глобал Инжиниринг",
    "Альфа Консалт",
    "Бета Системс",
    "МегаТрон",
    "ИнноваЛаб",
    "Стратегия+",
    "ЭнергоПроект",
    "Диджитал Групп",
    "Форсайт",
]

PROJECT_NAMES = [
    "Разработка CRM",
    "Миграция на облако",
    "Оптимизация процессов",
    "ERP-интеграция",
    "Веб-платформа 2.0",
    "Автоматизация склада",
    "BI-отчетность",
    "Мобильное приложение",
    "Кибербезопасность",
    "AI-аналитика",
]

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

organizations: list[dict] = [
    {"name": "Organizaton_01"},
    {"name": "Organizaton_02"},
    {"name": "Organizaton_03"},
    {"name": "Organizaton_04"},
    {"name": "Organizaton_05"},
    {"name": "Organizaton_06"},
]

divisions = [
    {
        "division": {
            "level_01": "Directorate",
            "level_02": "Department",
            "level_03": "Sector",
            "level_04": "Group",
        },
        "organization_id": random.randint(1, 10),
    },
    {
        "division": {
            "level_01": "Directorate",
            "level_02": "Department",
            "level_03": "Sector",
            "level_04": "Group",
        },
        "organization_id": random.randint(1, 10),
    },
]

users = [
    {
        "last_name": random.choice(LAST_NAMES),
        "first_name": random.choice(FIRST_NAMES),
        "patronymic": random.choice(PATRONYMICS),
        "email": faker.email(),
        "password": "qwe",
        "division_id": 5,
    },
    {
        "last_name": random.choice(LAST_NAMES),
        "first_name": random.choice(FIRST_NAMES),
        "patronymic": random.choice(PATRONYMICS),
        "email": faker.email(),
        "password": "qwe",
        "division_id": 5,
    },
]

projects = [
    {
        "name": random.choice(PROJECT_NAMES),
        "completed": False,
        "organization_id": random.randint(1, 10),
    },
    {
        "name": random.choice(PROJECT_NAMES),
        "completed": False,
        "organization_id": random.randint(1, 10),
    },
]

activity_types = [
    {
        "name": random.choice(ACTIVITY_TYPES),
        "organization_id": random.randint(1, 10),
        "visible": True,
    },
    {
        "name": random.choice(ACTIVITY_TYPES),
        "organization_id": random.randint(1, 10),
        "visible": True,
    },
]

tasks = [
    {
        "user_id": 1,
        "project_id": 1,
        "type_of_activity_id": 1,
        "start_time": datetime(
            year=2025,
            month=9,
            day=23,
            hour=10,
            minute=0,
            second=0,
        ),
        "end_time": datetime(
            year=2025,
            month=10,
            day=15,
            hour=18,
            minute=0,
            second=0,
        ),
        "description": "To do anything",
    },
    {
        "user_id": 2,
        "project_id": 2,
        "type_of_activity_id": 2,
        "start_time": datetime(
            year=2025,
            month=9,
            day=23,
            hour=10,
            minute=0,
            second=0,
        ),
        "end_time": datetime(
            year=2025,
            month=10,
            day=15,
            hour=18,
            minute=0,
            second=0,
        ),
        "description": "To do anything",
    },
]
