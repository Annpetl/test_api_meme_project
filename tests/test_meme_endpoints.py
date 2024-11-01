import pytest
from test_data import CREATE_BODY, CREATE_NEGATIVE_BODY, UPDATE_BODY


def test_authorize(meme_authorize_request):
    meme_authorize_request.authorize(body={"name": "Hanna"})
    meme_authorize_request.assert_status_200()
    meme_authorize_request.assert_response_len(2)


def test_authorize_with_empty_body(meme_authorize_request):
    meme_authorize_request.authorize(body={})
    meme_authorize_request.assert_status_400()


def test_authorize_with_invalid_body(meme_authorize_request):
    meme_authorize_request.authorize(body={"name": ["Hanna"]})
    meme_authorize_request.assert_status_400()


def test_if_token_valid(meme_authorize_request):
    meme_authorize_request.is_token_valid()


def test_create_meme(authorize_token, meme_post_request, meme_delete_request):
    meme_post_request.create(authorize_token, body=CREATE_BODY)
    meme_post_request.assert_status_200()
    meme_post_request.assert_response_len(6)
    meme_post_request.assert_response_tags(CREATE_BODY['tags'])
    meme_post_request.assert_response_text(CREATE_BODY['text'])
    meme_post_request.assert_response_info(CREATE_BODY['info'])
    meme_post_request.assert_response_url(CREATE_BODY['url'])
    meme_delete_request.delete(meme_post_request.json['id'], authorize_token)


@pytest.mark.parametrize('body', CREATE_NEGATIVE_BODY)
def test_create_meme_with_invalid_body(authorize_token, meme_post_request, body):
    meme_post_request.create(authorize_token, body=body)
    meme_post_request.assert_status_400()


def test_meme_unauthorized(meme_post_request, meme_get_request, meme_put_request, meme_delete_request, meme_id):
    meme_get_request.get_all(None)
    meme_get_request.assert_status_401()
    meme_post_request.create(token=None, body=CREATE_BODY)
    meme_post_request.assert_status_401()
    meme_put_request.update(token=None, meme_id=meme_id, body=UPDATE_BODY)
    meme_put_request.assert_status_401()
    meme_delete_request.delete(token=None, meme_id=meme_id)
    meme_delete_request.assert_status_401()


def test_get_all_memes(authorize_token, meme_get_request):
    meme_get_request.get_all(authorize_token)
    meme_get_request.assert_status_200()


def test_get_meme_by_id(authorize_token, meme_get_request, meme_id):
    meme_get_request.get_by_id(token=authorize_token, meme_id=meme_id)
    meme_get_request.assert_status_200()
    meme_get_request.assert_response_id(meme_id)
    meme_get_request.assert_response_len(6)


def test_get_meme_by_invalid_id(authorize_token, meme_get_request):
    meme_get_request.get_by_id(token=authorize_token, meme_id='meme_id')
    meme_get_request.assert_status_404()


def test_invalid_http_method(authorize_token, meme_id, meme_put_request):
    meme_put_request.assert_status_405_with_invalid_http_method(token=authorize_token, meme_id=meme_id,
                                                                body=UPDATE_BODY)


def test_update_meme(authorize_token, meme_put_request, meme_id):
    meme_put_request.update(token=authorize_token, meme_id=meme_id, body=UPDATE_BODY)
    meme_put_request.assert_status_200()
    meme_put_request.assert_response_len(6)
    meme_put_request.assert_response_tags(UPDATE_BODY['tags'])
    meme_put_request.assert_response_text(UPDATE_BODY['text'])
    meme_put_request.assert_response_info(UPDATE_BODY['info'])
    meme_put_request.assert_response_id(meme_id)


def test_delete_meme(authorize_token, meme_delete_request, meme_id, meme_get_request):
    meme_delete_request.delete(token=authorize_token, meme_id=meme_id)
    meme_delete_request.assert_status_200()
    meme_get_request.get_by_id(token=authorize_token, meme_id=meme_id)
    meme_get_request.assert_status_404()


def test_delete_meme_by_invalid_id(meme_delete_request, authorize_token):
    meme_delete_request.delete(token=authorize_token, meme_id='meme_id')
    meme_delete_request.assert_status_404()
