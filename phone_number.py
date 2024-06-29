import requests
from rich import print

from helpers import create_headers

post_user_phone_url = "https://internal-gateway.storicarddev.com/v1/users/phone_numbers"

get_phone_numbers_url = (
    lambda user_id: f"https://internal-gateway.storicarddev.com/v1/users/{user_id}/phone_numbers"
)

post_phone_number = "https://internal-gateway.storicarddev.com/v1/users/phone_numbers"


def post_phone_payload(user_id, phone_number):
    return {
        "user_id": user_id,
        "phone": {
            "country_code": "+52",
            "phone_number": phone_number.replace("+52", ""),
            "is_verified": True,
            "type": "PRIMARY",
        },
    }


def get_phone_numbers(decoded_token):
    headers = create_headers(decoded_token)
    r = requests.get(get_phone_numbers_url(decoded_token["user_id"]), headers=headers)
    return r.json()


def send_phone_number(decoded_token, phone_number=None):
    user_id = decoded_token["user_id"]
    if phone_number:
        phone = phone_number
    if decoded_token["phone_number"]:
        phone = decoded_token["phone_number"]
    else:
        if not phone_number:
            return "[bold red]Phone number not found in decoded_token and not provided[/bold red]"
        else:
            return "[bold red]Phone number not found in decoded_token[/bold red]"
    payload = post_phone_payload(user_id, phone)
    headers = create_headers(decoded_token)
    r = requests.post(post_user_phone_url, headers=headers, json=payload)
    return r.json()
