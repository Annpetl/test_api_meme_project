import os
import allure

from dotenv import load_dotenv


@allure.step('read value in env file')
def read(key):
    load_dotenv()
    return os.getenv(f'{key}')


@allure.step('change value in env file')
def update(key, value):
    with open('.env', 'w') as file:
        file.write(f'{key} = {value}')
