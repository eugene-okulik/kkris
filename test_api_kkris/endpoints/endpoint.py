import allure


class Endpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None


    @allure.step("Check that title is the same")
    def check_response_title(self, name):
        assert self.json['name'] == name, 'Wrong body name returned'


    @allure.step("Check that response code is 200")
    def check_response_code(self):
        assert self.response.status_code == 200, 'Wrong status code returned'
