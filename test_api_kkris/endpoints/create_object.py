import allure
import requests
from endpoints.endpoint import Endpoint


class CreateObject(Endpoint):


    @allure.step("Create new object")
    def create_new_object(self, payload, headers):
        self.response = requests.post(self.url, json=payload, headers=headers)
        self.json = self.response.json()
        return self.response
