import requests
from classes.base_endpoint import Endpoint


class CreateMemeRequest(Endpoint):

    def create(self, token, body):
        self.response = requests.post(f'{Endpoint.base_url}/meme', json=body,
                                      headers={"Authorization": f"{token}"})
        if self.response.status_code == 200:
            self.json = self.response.json()

