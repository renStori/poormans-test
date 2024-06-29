from random import randrange

import click
from rich import print

from device_session import send_session_data
from phone_number import get_phone_numbers, send_phone_number
from token_tools import get_token, process_token
from users import retrieve_user_id, send_post_user


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

    if not decoded_token.get("phone_number"):
        return print("[bold red]Token do not contains phone_number.[/bold red]")

    # Send device session
    session_data_response = send_session_data(decoded_token)
    print(session_data_response)

    # Check if user exist on Platform
    platform_user_data = retrieve_user_id(decoded_token)
    print(platform_user_data)
    if platform_user_data["code"] == 404:
        platform_user_data = send_post_user(decoded_token)
        if platform_user_data["code"] == 201:
            print(platform_user_data)
            return print("[bold blue]User created in Platform[/bold blue]")

    # Check if user has a phone in platform
    user_phone_number = get_phone_numbers(decoded_token)
    print(user_phone_number)
    if user_phone_number["status"] == "OK" and user_phone_number.get("data"):
        if len(user_phone_number["data"].get("phone_numbers")):
            return print(
                "[bold red]User has a phone number already registered.[/bold red]"
            )

    # Send phone number
    phone_number_response = send_phone_number(decoded_token)
    print(phone_number_response)

    if phone_number_response.get("code") == 409:
        phone = str(randrange(1000000000, 9999999999))
        print(f"[yellow]Generated phone: {phone}[/yellow]")
        phone_number_response = send_phone_number(decoded_token, phone)
        print(phone_number_response)


if __name__ == "__main__":
    main()
