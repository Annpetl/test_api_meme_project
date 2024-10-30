import requests
import allure

from classes import env_service
from classes.base_endpoint import Endpoint

_TOKEN = "TOKEN"


class Token:

    def __init__(self):
        self.__auth_token = env_service.read(_TOKEN)

    @allure.step("generate new token in case it doesn't exist or it's invalid otherwise return existing token")
    def get(self):
        if not self.__auth_token or self.__is_expired():
            self.__get_new_token()
        return self.__auth_token

    @allure.step("generate new token ")
    def __get_new_token(self):
        response = requests.post(f'{Endpoint.base_url}/authorize', json={"name": "Hanna"}).json()
        self.__auth_token = response['token']
        env_service.update(_TOKEN, self.__auth_token)
        return self.__auth_token

    @allure.step("return 404 status code if token is expired")
    def __is_expired(self):
        response = requests.get(f"{Endpoint.base_url}/authorize/{self.__auth_token}")
        return response.status_code == 404
