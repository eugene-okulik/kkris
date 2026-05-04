import allure
import requests
from endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step("Delete object")
    def delete_existing_object(self, object_id):
        self.response = requests.delete(f'{self.url}/{object_id}')
        return self.response
