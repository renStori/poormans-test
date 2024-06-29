from random import randrange

import requests

from helpers import create_headers, platform_url

users_url = f"{platform_url}/users"
get_users_url = lambda user_id: f"{users_url}/{user_id}"


def post_user_payload(decoded_token):
    user_id = decoded_token["user_id"]
    email = decoded_token["email"]
    phone = str(randrange(1000000000, 9999999999))
    return {
        "email": email,
        "cognito_user_id": user_id,
        "status": "APPLICANT",
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
    r = requests.get(get_users_url(decoded_token["user_id"]), headers=headers)
    return r.json()
