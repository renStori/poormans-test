from random import randrange

import requests

from helpers import create_headers, platform_url

users_url = f"{platform_url}/users"
user_url = lambda user_id: f"{users_url}/{user_id}"


def patch_user(decoded_token, field, value):
    user_id = decoded_token["user_id"]
    payload = {field: value}
    r = requests.patch(
        user_url(user_id), headers=create_headers(decoded_token), json=payload
    )
    return r.json()


def post_user_payload(decoded_token):
    user_id = decoded_token["user_id"]
    email = decoded_token["email"]
    phone = str(randrange(1000000000, 9999999999))
    return {
        "email": email,
        "cognito_user_id": user_id,
        "status": "APPLICANT",
        "db_source": "disrupt",
        "phone": {
            "country_code": "+52",
            "phone_number": phone,
            "is_verified": True,
        },
    }


def send_post_user(decoded_token):
    headers = create_headers(decoded_token)
    payload = post_user_payload(decoded_token)
    r = requests.post(users_url, headers=headers, json=payload)
    return r.json()


def retrieve_user_id(decoded_token):
    headers = create_headers(decoded_token)
    r = requests.get(user_url(decoded_token["user_id"]), headers=headers)
    return r.json()
