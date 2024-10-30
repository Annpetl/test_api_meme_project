import requests


class Endpoint:
    base_url = 'http://167.172.172.115:52355'
    response = None
    json = None

    def assert_status_200(self):
        assert self.response.status_code == 200

    def assert_status_400(self):
        assert self.response.status_code == 400

    def assert_status_404(self):
        assert self.response.status_code == 404

    @staticmethod
    def assert_status_405(meme_id, body, token):
        return requests.post(f'{Endpoint.base_url}/meme/{meme_id}', json=body,
                             headers={"Authorization": f"{token}"}).status_code == 405

    def assert_response_len(self):
        return len(self.json) == 6, f'actual response id is {len(self.json)}, expected 6'

    def assert_response_tags(self, tags):
        assert self.json['tags'] == tags, f'actual response id is {self.json['tags']}, expected {tags}'

    def assert_response_text(self, text):
        assert self.json['text'] == text, f'actual response id is {self.json['text']}, expected {text}'

    def assert_response_url(self, url):
        assert self.json['url'] == url, f'actual response id is {self.json['url']}, expected {url}'

    def assert_response_info(self, info):
        assert self.json['info'] == info, f'actual response id is {self.json['info']}, expected {info}'

    def assert_response_id(self, meme_id):
        assert int(self.json['id']) == int(meme_id), f'actual response id is {self.json['id']}, expected {meme_id}'
