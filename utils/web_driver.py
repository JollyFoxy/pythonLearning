import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class WebDriver:
    _options = Options()

    _options.page_load_strategy = "normal"

    _options.add_argument = "--headless"
    _options.add_argument = "--lang=ru"
    _options.add_argument = "--disable-dev-shm-usage"

    prefs = {"download.default_directory": os.path.abspath("data")}
    _options.add_experimental_option("prefs", prefs)

    _driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=_options)

    def get_web_driver(self):
        return self._driver
