from uuid import uuid4


def generate_uuid() -> str:
    return str(uuid4())


def create_headers(decoded_token):
    return {
        "Authorization": f"{decoded_token['auth_type']} {decoded_token['id_token']}",
        "X-Api-Key": "G9anHkrQMT30HMjfj3You3TU6oQ2OGdb46juf6BO",
        "X-Ad-Device-Id": "6b209118-3e44-44c2-87bb-ee00f57d281a",
        "App-Version": "0.0.107",
        "Operative-System": "13",
        "Os-Version": "13",
        "Platform-Version": "Android",
        "Platform": "Android",
        "Content-Type": "application/json; charset=UTF-8",
        "Accept-Encoding": "gzip, deflate, br",
        "User-Agent": "okhttp/5.0.0-alpha.3",
    }
