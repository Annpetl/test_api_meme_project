from classes.base_endpoint import Endpoint
import requests


class GetMemeRequest(Endpoint):

    def get_all(self, token):
        self.response = requests.get(f'{Endpoint.base_url}/meme', headers={"Authorization": f"{token}"})

    def get_by_id(self, token, meme_id):
        self.response = requests.get(f'{Endpoint.base_url}/meme/{meme_id}', headers={"Authorization": f"{token}"})
        if self.response.status_code == 200:
            self.json = self.response.json()
        return self.response
