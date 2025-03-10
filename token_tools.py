import json

import jwt
import requests

url = "https://dev-api.storicarddev.com/idp/idp/cf"


def get_token(email, password=None):
    if not password:
        password = "Holamundo1"
    payload = {
        "AuthFlow": "USER_PASSWORD_AUTH",
        "AuthParameters": {"PASSWORD": password, "USERNAME": email},
        "ClientId": "2hd3pqt5687oo7co4o24ligojj",
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-amz-json-1.1",
        "X-Amz-Target": "AWSCognitoIdentityProviderService.InitiateAuth",
    }
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    return r.json()


def process_token(access_token):
    auth_type = access_token["AuthenticationResult"]["TokenType"]
    id_token = access_token["AuthenticationResult"]["IdToken"]
    decoded_token = jwt.decode(
        bytes(id_token, "utf-8"), options={"verify_signature": False}
    )

    return {
        "auth_type": auth_type,
        "id_token": id_token,
        "user_id": decoded_token.get("sub"),
        "email": decoded_token.get("email"),
        "phone_number": decoded_token.get("phone_number"),
    }
