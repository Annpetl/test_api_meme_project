import requests
import allure
from classes import env_service
from classes.base_endpoint import Endpoint

_TOKEN = "TOKEN"


class Token(Endpoint):

    def __init__(self):
        self.__auth_token = env_service.read(_TOKEN)

    @allure.step("generate new token in case it doesn't exist or it's invalid otherwise return existing token")
    def get(self):
        if not self.__auth_token or not self.is_token_valid():
            self.__get_new_token()
        return self.__auth_token

    @allure.step("generate new token ")
    def __get_new_token(self):
        self.response = self.authorize(body={"name": "Hanna"})
        self.__auth_token = self.response['token']
        env_service.update(_TOKEN, self.__auth_token)
        return self.__auth_token

    @allure.step("return 200 status code if token is valid")
    def is_token_valid(self):
        self.response = requests.get(f"{Endpoint.base_url}/authorize/{self.__auth_token}")
        return self.response.status_code == 200

    def authorize(self, body):
        self.response = requests.post(f'{Endpoint.base_url}/authorize', json=body)
        if self.response.status_code == 200:
            self.json = self.response.json()
            return self.json
