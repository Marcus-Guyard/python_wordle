import requests
from pprint import pprint

GOREST_USERS = "https://gorest.co.in/public/v2/users"

GOREST_POSTS = "https://gorest.co.in/public/v2/posts"

GOREST_COMMENTS = "https://gorest.co.in/public/v2/comments"


def api_token() -> str:
    with open("token") as f:
        return f.read().strip()

header = {"authorization": f"Bearer {api_token()}"}

userdata = {"name": "new tester",
            "email": "newtester@email.com",
            "gender": "male",
            "status": "active"}


def create_user(user_data: dict) -> dict:
    res = requests.post("%s" % GOREST_USERS, data=userdata, headers=header)
    return res.json()


def patch_user(user_id) -> dict:
    res = requests.patch(f"{GOREST_USERS}/{user_id}", data=userdata, headers=header)
    return res.json()


def get_all_users() -> dict:
    res = requests.get(f"{GOREST_USERS}", headers=header)
    return res.json()


def get_user(user_id: int) -> dict:
    res = requests.get(f"{GOREST_USERS}/{user_id}", headers=header)
    return res.json()


def get_all_comments() -> dict:
    res = requests.get(f"{GOREST_COMMENTS}", headers=header)
    return res.json()


def get_all_posts() -> dict:
    res = requests.get(f"{GOREST_POSTS}", headers=header)
    return res.json()


def delete_user(user_id: int) -> str:
    deleted_user = requests.get(f"{GOREST_USERS}/{user_id}", headers=header).json()
    requests.delete(f"{GOREST_USERS}/{user_id}", headers=header)
    return f"Deleted: {deleted_user}"

if __name__ == '__main__':
    pprint(get_all_users())


