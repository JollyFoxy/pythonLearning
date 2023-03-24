import pytest
from api.api_client import ApiClient


@pytest.fixture
def input_value():
    input = 39
    return input


@pytest.fixture()
def dog_base_url():
    return ApiClient(base_path="https://dog.ceo/api/")
