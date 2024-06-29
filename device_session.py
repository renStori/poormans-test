from datetime import datetime as dt

import requests

from helpers import create_headers, generate_uuid
from token_tools import get_token, process_token

url = "https://dev-api.storicarddev.com/device/session"


def session_payload(user_id):
    now = dt.utcnow()
    ts = int(now.timestamp() * 1000)
    ts_string = now.isoformat()
    return {
        "action": "click",
        "app_version": "0.0.107",
        "appl_id": 0,
        "current_page": "sign_in_page",
        "device_id": generate_uuid(),
        "device_type": "android",
        "event_ts": ts,
        "event_ts_readable": ts_string,
        "from_page": "",
        "item_selected": "sign_in_button",
        "product_id": "stori",
        "session_id": generate_uuid(),
        "user_id": user_id,
    }


def send_session_data(decoded_token):
    headers = create_headers(decoded_token)
    payload = session_payload(decoded_token["user_id"])
    r = requests.post(url, headers=headers, json=payload)
    return r.json()
