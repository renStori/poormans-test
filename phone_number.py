import requests
from rich import print

from helpers import create_headers

url = "https://internal-gateway.storicarddev.com/v1/users/phone_numbers"


def phone_payload(user_id, phone_number):
    return {
        "user_id": user_id,
        "phone": {
            "country_code": "+52",
            "phone_number": phone_number.replace("+52", ""),
            "is_verified": True,
            "type": "PRIMARY",
        },
    }


def send_phone_number(decoded_token):
    payload = phone_payload(decoded_token["user_id"], decoded_token["phone_number"])
    headers = create_headers(decoded_token)
    r = requests.post(url, headers=headers, json=payload)
    return r.json()
