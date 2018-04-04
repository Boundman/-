import requests
from base_class import *


class getId(BaseClient):
    BASE_URL = 'https://api.vk.com/method/'
    method = 'users.get?user_ids='
    http_method = 'get'
    rest_url_code = '&fields=bdate&v=5.73'

    def __init__(self, username):
        self.username = username
        self.parameters = (('user_ids', username), ('fields', 'bdate'))

    def get_params(self):
        return self.parameters

    def generate_url(self, method):
        return '{}{}{}{}'.format(self.BASE_URL, self.method, self.username, self.rest_url_code)

    def _get_data(self, method, http_method):
        try:
            # response = requests[http_method](generate_url(method), params = self.get_params())
            response = requests.get(self.generate_url(method), params=self.get_params())
        except ConnectionError:
            print('Неудачная попытка отправки запроса')
        else:
            return self.response_handler(response)

    def response_handler(self, response):
        return response

    def execute(self):
        return self._get_data(
            self.method,
            http_method=self.http_method
        )
