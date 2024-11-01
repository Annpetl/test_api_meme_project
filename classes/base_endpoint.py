import requests


class Endpoint:
    base_url = 'http://167.172.172.115:52355'
    response = None
    json = None

    def assert_status_200(self):
     assert self.response.status_code == 200, f'AR is {self.response.status_code}, ER 200'

    def assert_status_400(self):
        assert self.response.status_code == 400, f'AR is {self.response.status_code}, ER 400'

    def assert_status_404(self):
        assert self.response.status_code == 404, f'AR is {self.response.status_code}, ER 404'

    def assert_status_405_with_invalid_http_method(self, meme_id, body, token):
        self.response = requests.post(f'{Endpoint.base_url}/meme/{meme_id}', json=body, headers={
            "Authorization": f"{token}"})
        assert self.response.status_code == 405, f'AR is {self.response.status_code}, ER 405'

    def assert_status_401(self):
        assert self.response.status_code == 401, f'AR is {self.response.status_code}, ER 401'

    def assert_response_len(self, length):
        return len(self.json) == length, f'AR is {len(self.json)}, ER {length}'

    def assert_response_tags(self, tags):
        assert self.json['tags'] == tags, f'AR is {self.json['tags']}, ER {tags}'

    def assert_response_text(self, text):
        assert self.json['text'] == text, f'AR is {self.json['text']}, ER {text}'

    def assert_response_url(self, url):
        assert self.json['url'] == url, f'AR is {self.json['url']}, ER {url}'

    def assert_response_info(self, info):
        assert self.json['info'] == info, f'AR is {self.json['info']}, ER {info}'

    def assert_response_id(self, meme_id):
        assert int(self.json['id']) == int(meme_id), f'AR is {self.json['id']}, ER {meme_id}'
