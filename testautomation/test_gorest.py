from http import HTTPStatus
import requests
from pprint import pprint
import pytest
from gorest import api_token as api

GOREST_USERS = "https://gorest.co.in/public/v2/users"
GOREST_POSTS = "https://gorest.co.in/public/v2/posts"
GOREST_COMMENTS = "https://gorest.co.in/public/v2/comments"
GOREST_TODOS = "https://gorest.co.in/public/v2/todos"

HEADER = {"Authorization": f"Bearer {api()}"}

userdata = {"name": "new tester",
            "email": "test@email.com",
            "gender": "male",
            "status": "active"}


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


def test_get_user():
    res = requests.post(GOREST_USERS, data=userdata, headers=HEADER)
    user_dict = res.json()
    get_user = requests.get(GOREST_USERS + f"/{user_dict['id']}", headers=HEADER)
    assert get_user.status_code == HTTPStatus.OK
    requests.delete(GOREST_USERS + f"/{user_dict['id']}", headers=HEADER)


def test_get_user_posts():
    res = requests.post(GOREST_USERS, data=userdata, headers=HEADER)
    user_dict = res.json()
    requests.post(GOREST_POSTS,
                  data={"user_id": user_dict['id'],
                        'title': 'Min titel',
                        'body': 'Detta är en post'},
                  headers=HEADER)
    get_user_posts = requests.get(GOREST_USERS + f"/{user_dict['id']}/posts", headers=HEADER)
    assert get_user_posts.status_code == HTTPStatus.OK
    requests.delete(GOREST_USERS + f"/{user_dict['id']}", headers=HEADER)


def test_get_user_comments():
    res = requests.post(GOREST_USERS, data=userdata, headers=HEADER)
    user_dict = res.json()
    new_post = requests.post(GOREST_POSTS,
                             data={"user_id": user_dict['id'],
                                   'title': 'Min titel',
                                   'body': 'Detta är en post'},
                             headers=HEADER)
    post_dict = new_post.json()
    requests.post(GOREST_COMMENTS,
                  data={"post_id": post_dict["id"],
                        "name": 'Commenter Name',
                        "email": 'commenter@email.com',
                        "body": 'This is a comment'},
                  headers=HEADER)

    get_user_comments = requests.get(GOREST_POSTS + f"/{post_dict['id']}/comments", headers=HEADER)
    assert get_user_comments.status_code == HTTPStatus.OK
    requests.delete(GOREST_USERS + f"/{user_dict['id']}", headers=HEADER)


def test_get_user_todos():
    res = requests.post(GOREST_USERS, data=userdata, headers=HEADER)
    user_dict = res.json()
    requests.post(GOREST_TODOS,
                  data={"user_id": user_dict['id'],
                        'title': 'TODO Title',
                        'status': 'pending'},
                  headers=HEADER)

    get_user_todos = requests.get(GOREST_USERS + f"/{user_dict['id']}/todos", headers=HEADER)
    assert get_user_todos.status_code == HTTPStatus.OK
    requests.delete(GOREST_USERS + f"/{user_dict['id']}", headers=HEADER)


def test_create_user():
    res = requests.post(GOREST_USERS, data=userdata, headers=HEADER)
    user_dict = res.json()
    assert res.status_code == HTTPStatus.CREATED
    requests.delete(GOREST_USERS + f"/{user_dict['id']}", headers=HEADER)


def test_create_post():
    new_user = requests.post(GOREST_USERS, data=userdata, headers=HEADER)
    user_dict = new_user.json()
    new_post = requests.post(GOREST_POSTS,
                             data={"user_id": user_dict['id'],
                                   'title': 'Min titel',
                                   'body': 'Detta är en post'},
                             headers=HEADER)

    assert new_post.status_code == HTTPStatus.CREATED
    requests.delete(GOREST_USERS + f"/{user_dict['id']}", headers=HEADER)


def test_create_comment():
    new_user = requests.post(GOREST_USERS, data=userdata, headers=HEADER)
    user_dict = new_user.json()
    new_post = requests.post(GOREST_POSTS,
                             data={"user_id": user_dict['id'],
                                   'title': 'Min titel',
                                   'body': 'Detta är en post'},
                             headers=HEADER)
    post_dict = new_post.json()
    new_comment = requests.post(GOREST_COMMENTS,
                                data={"post_id": post_dict["id"],
                                      "name": 'Commenter Name',
                                      "email": 'commenter@email.com',
                                      "body": 'This is a comment'},
                                headers=HEADER)

    assert new_comment.status_code == HTTPStatus.CREATED
    requests.delete(GOREST_USERS + f"/{user_dict['id']}", headers=HEADER)


def test_create_todo():
    new_user = requests.post(GOREST_USERS, data=userdata, headers=HEADER)
    user_dict = new_user.json()
    new_todo = requests.post(GOREST_TODOS,
                             data={"user_id": user_dict['id'],
                                   'title': 'TODO Title',
                                   'status': 'pending'},
                             headers=HEADER)
    todo_dict = new_todo.json()

    assert new_todo.status_code == HTTPStatus.CREATED
    requests.delete(GOREST_USERS + f"/{todo_dict['user_id']}", headers=HEADER)


def test_patch_user():
    new_user = requests.post(GOREST_USERS, data=userdata, headers=HEADER)
    user_dict = new_user.json()
    patch = requests.patch(GOREST_USERS + f"/{user_dict['id']}",
                           data={'name': 'Patched Name',
                                 'email': 'Patched@name.com',
                                 'status': 'inactive'},
                           headers=HEADER)

    assert patch.status_code == HTTPStatus.OK
    requests.delete(GOREST_USERS + f"/{user_dict['id']}", headers=HEADER)


def test_put_user():
    new_user = requests.post(GOREST_USERS, data=userdata, headers=HEADER)
    user_dict = new_user.json()
    put = requests.put(GOREST_USERS + f"/{user_dict['id']}",
                       data={'name': 'Putted Name',
                             'email': 'Putted@name.com',
                             'status': 'inactive'},
                       headers=HEADER)

    assert put.status_code == HTTPStatus.OK
    requests.delete(GOREST_USERS + f"/{user_dict['id']}", headers=HEADER)
