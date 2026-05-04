import allure
import requests
from endpoints.endpoint import Endpoint


class GetObject(Endpoint):

    @allure.step("Get all objects")
    def get_all_objects(self):
        self.response = requests.get(self.url)
        self.json = self.response.json()
        return self.response

    @allure.step("Check that all objects returned")
    def check_object_len(self):
        assert len(self.json) == 1, 'Not all objects returned'

    @allure.step("Get object by id")
    def get_object_by_id(self, object_id):
        self.response = requests.get(f'{self.url}/{object_id}')
        self.json = self.response.json()
        return self.response

    @allure.step("Check that correct object_id returned")
    def check_object_id_is_correct(self, object_id):
        assert self.json['id'] == object_id, 'Wrong object id returned'
