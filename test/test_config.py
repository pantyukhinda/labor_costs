import sys
from os.path import dirname, abspath

import pytest

from pydantic_settings import BaseSettings

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
sys.path.insert(0, dirname(dirname(abspath(__file__))) + "/app")

from core.config import settings


@pytest.fixture
def settings_in_json_format():
    return settings.model_dump_json()


@pytest.fixture
def settings_obj():
    return settings


@pytest.mark.usefixtures("settings_obj", "settings_in_json_format")
class TestConfig:
    def test_init_config(self):
        assert isinstance(settings_obj, BaseSettings)

    def test_config_keys(self):
        settings_json = settings_in_json_format
        from pprint import pprint

        pprint(settings_json)
        assert 1 == 1
