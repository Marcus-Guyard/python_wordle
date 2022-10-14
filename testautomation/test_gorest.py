from http import HTTPStatus
import requests
import pytest

GOREST_USERS = "https://gorest.co.in/public/v2/users"
GOREST_POSTS = "https://gorest.co.in/public/v2/posts"
GOREST_COMMENTS = "https://gorest.co.in/public/v2/comments"


@pytest.fixture
def api_token() -> str:
    with open("token") as f:
        return f.read().strip()


@pytest.fixture
def header():
    return {"authorization": f"Bearer {api_token}"}

HEADER = {"authorization": f"Bearer {api_token}"}


@pytest.fixture
def user_adata():
    return {"name": "new tester",
            "email": "test@email.com",
            "gender": "male",
            "status": "active"}

userdata = {"name": "new tester",
            "email": "test@email.com",
            "gender": "male",
            "status": "active"}


def test_get_all_users():
    res = requests.get(GOREST_USERS, headers=HEADER)
    assert res.status_code == HTTPStatus.OK


def test_create_user_v2():
    res = requests.post(GOREST_USERS, data=userdata, headers=HEADER)
    user_dict = res.json()
    assert res.status_code == HTTPStatus.CREATED
    requests.delete(GOREST_USERS + f"/{user_dict['id']}", headers=HEADER)


def test_create_post(userdata, HEADER):
    new_user = requests.post(GOREST_USERS, data=userdata, header=HEADER).json()
    new_post = requests.post(GOREST_POSTS,
                             data={"user_id": new_user['id'],
                                   'title': 'Min titel',
                                   'body': 'detta är min body'},
                             headers=HEADER)

    assert new_post.status_code == HTTPStatus.CREATED
    requests.delete(GOREST_POSTS + f"/{new_post.json()['id']}", headers=HEADER)
    requests.delete(GOREST_USERS + f"/{new_user['id']}", headers=HEADER)


# def test_create_user():
#     res = requests.post(GOREST_USERS, data={"name": "new tester",
#                                             "email": "newtester@email.com",
#                                             "gender": "male",
#                                             "status": "active"},
#                         headers=HEADER)
#     user_json = res.json()
#     assert res.status_code == HTTPStatus.CREATED
#     assert 'name' in user_json
#     assert 'email' in user_json
#     assert 'gender' in user_json
#     assert 'status' in user_json
#     assert 'id' in user_json
#     requests.delete(GOREST_USERS + f"/{user_json['id']}", headers=HEADER)

