import requests
from classes.base_endpoint import Endpoint


class DeleteMemeRequest(Endpoint):
    def delete(self, meme_id, token):
        self.response = requests.delete(f'{Endpoint.base_url}/meme/{meme_id}', headers={"Authorization": f"{token}"})


