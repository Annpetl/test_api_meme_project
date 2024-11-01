import pytest
from classes.auth_token import Token
from classes.create_meme import CreateMemeRequest
from classes.delete_meme import DeleteMemeRequest
from classes.get_meme import GetMemeRequest
from classes.update_meme import UpdateMemeRequest
from classes.auth_token import Token


@pytest.fixture()
def meme_authorize_request():
    return Token()


@pytest.fixture()
def meme_post_request():
    return CreateMemeRequest()


@pytest.fixture()
def meme_get_request():
    return GetMemeRequest()


@pytest.fixture()
def meme_put_request():
    return UpdateMemeRequest()


@pytest.fixture()
def meme_delete_request():
    return DeleteMemeRequest()


@pytest.fixture()
def meme_id(meme_post_request, authorize_token, meme_delete_request):
    body = {
        "text": "code error don't disappears after 10 times reload",
        "url": "https://cs14.pikabu.ru/post_img/big/2024/04/17/4/1713327862183782924.png",
        "tags": ["code errors"],
        "info": {"meme_topic": "code errors"}
    }
    meme_post_request.create(authorize_token, body=body)
    meme_id = meme_post_request.json['id']
    yield meme_id
    meme_delete_request.delete(meme_id, authorize_token)


@pytest.fixture()
def authorize_token():
    return Token().get()
