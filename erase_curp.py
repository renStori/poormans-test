import click
from rich import print

from device_session import send_session_data
from helpers import not_a_curp
from token_tools import get_token, process_token
from users import patch_user, retrieve_user_id


@click.command()
@click.option("--email", required=True)
@click.option("--password", required=False)
def main(email, password):
    # Get access_token
    access_token = get_token(email, password)
    print(access_token)

    # Decode Token
    decoded_token = process_token(access_token)
    print(decoded_token)

    # Send device session
    # session_data_response = send_session_data(decoded_token)
    # print(session_data_response)

    patch = patch_user(decoded_token, "curp", not_a_curp())
    print(patch)

    user_data = retrieve_user_id(decoded_token)
    print(user_data)
    return user_data


if __name__ == "__main__":
    main()
