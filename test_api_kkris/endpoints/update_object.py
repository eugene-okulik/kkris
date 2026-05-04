import allure
import requests
from endpoints.endpoint import Endpoint


class UpdateObject(Endpoint):


    @allure.step("Update (put) existing object")
    def put_existing_object(self, object_id, payload, headers):
        self.response = requests.put(f'{self.url}/{object_id}', json=payload, headers=headers)
        self.json = self.response.json()
        return self.response


    @allure.step("Update (patch) existing object")
    def patch_existing_object(self, object_id, payload, headers):
        self.response = requests.patch(f'{self.url}/{object_id}', json=payload, headers=headers)
        self.json = self.response.json()
        return self.response
