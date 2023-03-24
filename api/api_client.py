import allure
import requests


class ApiClient:
    def __init__(self, base_path):
        self.base_path = base_path

    def get(self, path="/", params=None, headers=None):
        url = f"{self.base_path}{path}"
        with allure.step(f"GET request to: {url}"):
            return requests.get(url=url, params=params, headers=headers)

    def post(self, path="/",  params=None, data=None, json=None, headers=None):
        url = f"f{self.base_path}{path}"
        with allure.step(f"POST request to: {url}"):
            return requests.post(url=url, params=params, data=data, json=json, headers=headers)
