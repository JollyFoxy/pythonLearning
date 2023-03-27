import pytest

import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from api.api_client import ApiClient


@pytest.fixture()
def get_driver():
    _options = Options()

    _options.page_load_strategy = "normal"

    _options.add_argument = "--headless"
    _options.add_argument = "--lang=ru"
    _options.add_argument = "--disable-dev-shm-usage"

    prefs = {"download.default_directory": os.path.abspath("data")}
    _options.add_experimental_option("prefs", prefs)

    _driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=_options)

    yield _driver


@pytest.fixture
def input_value():
    input = 39
    return input


@pytest.fixture
def dog_base_url():
    return ApiClient(base_path="https://dog.ceo/api/")


@pytest.fixture
def before(driver=get_driver):
    driver.get("https://demoqa.com/")
    driver.maximize_window()
