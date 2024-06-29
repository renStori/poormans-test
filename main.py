from rich import print

from device_session import send_session_data
from phone_number import send_phone_number
from token_tools import get_token, process_token

email = "jose72@yopmail.com"

# Get access_token
access_token = get_token(email)

# Decode Token
decoded_token = process_token(access_token)

# Send device session
send_session_data(decoded_token)

# Send phone number
send_phone_number(decoded_token)
