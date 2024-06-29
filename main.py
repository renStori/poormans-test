import click
from rich import print

from device_session import send_session_data
from phone_number import send_phone_number
from token_tools import get_token, process_token


@click.command()
@click.option("--email", required=True, help="Email address to use for the session")
def main(email):
    # Get access_token
    access_token = get_token(email)
    print(access_token)

    # Decode Token
    decoded_token = process_token(access_token)
    print(decoded_token)

    # Send device session
    session_data_response = send_session_data(decoded_token)
    print(session_data_response)

    # Send phone number
    phone_number_response = send_phone_number(decoded_token)
    print(phone_number_response)


if __name__ == "__main__":
    main()
