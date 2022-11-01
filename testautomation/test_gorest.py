from http import HTTPStatus
import requests
import pytest
from gorest import api_token as api

from data_model import User

GOREST_USERS = "https://gorest.co.in/public/v2/users"
GOREST_POSTS = "https://gorest.co.in/public/v2/posts"
GOREST_COMMENTS = "https://gorest.co.in/public/v2/comments"
GOREST_TODOS = "https://gorest.co.in/public/v2/todos"

HEADER = {"Authorization": f"Bearer {api()}"}

userdata = {"name": "new tester",
            "email": "test@email.com",
            "gender": "male",
            "status": "active"}

LIST_OF_USERS = [{"name": "new tester1",
                  "email": "test1@email.com",
                  "gender": "male",
                  "status": "active"},
                 {"name": "new tester2",
                  "email": "test2@email.com",
                  "gender": "male",
                  "status": "active"},
                 {"name": "new tester3",
                  "email": "test3@email.com",
                  "gender": "male",
                  "status": "active"}]

LIST_OF_USERS_AND_STATUS_CODE = [
    ({"name": "Testperson Testsson",
      "email": "endf@enmladres4s.se",
      "gender": "male",
      "status": "active"}, HTTPStatus.CREATED),
    ({"name": "En anna person",
      "email": "endf@enmladres4.se",
      "gender": "female",
      "status": "active"}, HTTPStatus.CREATED),
    ({"name": "Ny Person",
      "email": "dennes@adress.se",
      "gender": "female",
      "status": "active"}, HTTPStatus.CREATED),
    ({"name": "Min Testuser",
      "email": "dennesadrss@outlook.se",
      "gender": "male",
      "status": "active"}, HTTPStatus.CREATED),
    ({"name": "Min Testuser",
      "gender": "male",
      "status": "active"}, HTTPStatus.UNPROCESSABLE_ENTITY),
    ({"name": "Min Testuser",
      "email": "dennesadrssoutlook.se",
      "gender": "male",
      "status": "active"}, HTTPStatus.CREATED)
]


@pytest.fixture
def new_user():
    user = requests.post(GOREST_USERS, data=userdata, headers=HEADER)
    yield user
    requests.delete(GOREST_USERS + f"/{user.json()['id']}", headers=HEADER)


@pytest.fixture
def new_post(new_user):
    post_data = {"user_id": new_user.json()['id'],
                 'title': 'Min titel',
                 'body': 'Detta är en post'}
    new_post_response = requests.post(GOREST_POSTS, data=post_data, headers=HEADER)
    yield new_post_response
    requests.delete(GOREST_POSTS + f"/{new_post_response.json()['user_id']}", headers=HEADER)


@pytest.fixture
def new_comment(new_user, new_post):
    comment_data = {"post_id": new_post.json()["id"],
                    "name": 'Commenter Name',
                    "email": 'commenter@email.com',
                    "body": 'This is a comment'}
    new_comment_response = requests.post(GOREST_COMMENTS, data=comment_data, headers=HEADER)
    yield new_comment_response
    requests.delete(GOREST_COMMENTS + f"/{new_comment_response.json()['id']}", headers=HEADER)


@pytest.fixture
def new_todo(new_user):
    todo_data = {"user_id": new_user.json()['id'],
                 'title': 'TODO Title',
                 'status': 'pending'}
    new_todo_response = requests.post(GOREST_TODOS, data=todo_data, headers=HEADER)
    yield new_todo_response
    requests.delete(GOREST_COMMENTS + f"/{new_todo_response.json()['id']}", headers=HEADER)


@pytest.fixture
def new_user_v2():
    userdata['email'] = 'tester2@email.com'
    user = requests.post(GOREST_USERS, data=userdata, headers=HEADER)
    yield user
    requests.delete(GOREST_USERS + f"/{user.json()['id']}", headers=HEADER)


@pytest.fixture
def make_user():
    created_users = []

    def _make_user(name: str, email: str, gender: str, status: str) -> tuple[requests.Response, User]:
        response = requests.post(GOREST_USERS, data={"name": name, "email": email, "gender": gender, "status": status},
                                 headers=HEADER)
        created_user = User(**response.json())
        created_users.append(created_user)
        return response, created_user

    yield _make_user
    for user in created_users:
        requests.delete(GOREST_USERS + f"/{user.id}", headers=HEADER)


@pytest.fixture
def make_user_request():
    created_users = []

    def _make_request(user_dict) -> requests.Response:
        response = requests.post(GOREST_USERS, data=user_dict,
                                 headers=HEADER)
        if response.status_code == HTTPStatus.CREATED:
            created_users.append(response.json())
        return response
    yield _make_request
    for user in created_users:
        requests.delete(GOREST_USERS + f"/{user['id']}", headers=HEADER)


@pytest.fixture(params=LIST_OF_USERS)
def user_data2(request):
    return request.param


@pytest.fixture
def user_data():
    return {'name': "En Testperson",
            "email": "some_mail@mail.fr",
            "gender": "male",
            "status": "active"}


def test_two_users(make_user):
    user1 = make_user("Användare 1", "afinaffa@email.com", "male", "active")
    user2 = make_user("Användare 2", "aduihawfb@email.com", "male", "active")
    print(user1)
    print(user2)


def test_create_user_with_param(user_data2, make_user):
    _, user = make_user(**user_data2)
    assert user.name == user_data2['name']
    assert user.email == user_data2['email']
    assert user.gender == user_data2['gender']
    assert user.status == user_data2['status']


@pytest.mark.parametrize("user_dict", LIST_OF_USERS)
def test_create_user_with_mark_param(user_dict, make_user):
    _, user = make_user(**user_dict)
    assert user.name == user_dict['name']
    assert user.email == user_dict['email']
    assert user.gender == user_dict['gender']
    assert user.status == user_dict['status']


@pytest.mark.parametrize("user_dict, status_code", LIST_OF_USERS_AND_STATUS_CODE)
def test_create_user_status_code(user_dict, status_code, make_user_request):
    response = make_user_request(user_dict)
    assert response.status_code == status_code, f"Expected {status_code} got {response.status_code}"


def test_new_user_v2_status_code(new_user_v2):
    assert new_user_v2.status_code == HTTPStatus.CREATED


def test_new_user_response_time(new_user):
    assert new_user.elapsed.microseconds < 1000000
    assert new_user.status_code == HTTPStatus.CREATED


def test_new_user_response_code(new_user):
    assert new_user.status_code == HTTPStatus.CREATED


def test_check_post_with_fixture(new_post):
    assert 'title' in new_post.json()


def test_check_post_user(new_user, new_post):
    assert new_user.json()['id'] == new_post.json()['user_id']


def test_response_code_new_user(new_user):
    assert new_user.elapsed.microseconds < 1000000
    assert new_user.status_code == HTTPStatus.CREATED


def test_get_all_users():
    res = requests.get(GOREST_USERS, headers=HEADER)
    assert res.status_code == HTTPStatus.OK


def test_get_all_posts():
    res = requests.get(GOREST_POSTS, headers=HEADER)
    assert res.status_code == HTTPStatus.OK


def test_get_all_comments():
    res = requests.get(GOREST_COMMENTS, headers=HEADER)
    assert res.status_code == HTTPStatus.OK


def test_get_all_todos():
    res = requests.get(GOREST_POSTS, headers=HEADER)
    assert res.status_code == HTTPStatus.OK


def test_get_user(new_user):
    get_user = requests.get(GOREST_USERS + f"/{new_user.json()['id']}", headers=HEADER)
    assert get_user.status_code == HTTPStatus.OK


def test_get_user_posts_status_code(new_post):
    get_user_posts = requests.get(GOREST_USERS + f"/{new_post.json()['user_id']}/posts", headers=HEADER)
    assert get_user_posts.status_code == HTTPStatus.OK


def test_get_user_comments(new_post):
    get_user_comments = requests.get(GOREST_POSTS + f"/{new_post.json()['user_id']}/comments", headers=HEADER)
    assert get_user_comments.status_code == HTTPStatus.OK


def test_get_user_todos(new_user):
    get_user_todos = requests.get(GOREST_USERS + f"/{new_user.json()['id']}/todos", headers=HEADER)
    assert get_user_todos.status_code == HTTPStatus.OK


def test_new_user_status_code(new_user):
    assert new_user.status_code == HTTPStatus.CREATED


def test_create_user(new_user):
    assert new_user.json()["name"] == userdata["name"]
    assert new_user.json()["email"] == userdata["email"]
    assert new_user.json()["gender"] == userdata["gender"]
    assert new_user.json()["status"] == userdata["status"]


def test_create_post_status_code(new_post):
    assert new_post.status_code == HTTPStatus.CREATED


def test_create_comment(new_comment):
    assert new_comment.status_code == HTTPStatus.CREATED


def test_create_todo(new_todo):
    assert new_todo.status_code == HTTPStatus.CREATED


def test_patch_user(new_user):
    patch = requests.patch(GOREST_USERS + f"/{new_user.json()['id']}",
                           data={'name': 'Patched Name',
                                 'email': 'Patched@name.com',
                                 'status': 'inactive'},
                           headers=HEADER)

    assert patch.status_code == HTTPStatus.OK


def test_put_user(new_user):
    put = requests.put(GOREST_USERS + f"/{new_user.json()['id']}",
                       data={'name': 'Putted Name',
                             'email': 'Putted@name.com',
                             'status': 'inactive'},
                       headers=HEADER)

    assert put.status_code == HTTPStatus.OK
