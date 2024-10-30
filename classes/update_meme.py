import requests
from classes.base_endpoint import Endpoint


class UpdateMemeRequest(Endpoint):
    def update(self, token, meme_id, body):
        body["id"] = meme_id
        self.response = requests.put(f'{Endpoint.base_url}/meme/{meme_id}', json=body,
                                     headers={"Authorization": f"{token}"})
        self.json = self.response.json()

