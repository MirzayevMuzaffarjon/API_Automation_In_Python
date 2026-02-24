import logging


def test_register_happy_flow(auth_client, endpoints, data):
    response = auth_client.send_request(
        method = "POST",
        url = f"{endpoints.base_url}{endpoints.endpoint_users_register}",
        json = data.register_happy_flow
    )
    auth_client.check_status_code(response=response, expected_status=201)

    clearing = auth_client.delete_account(token=auth_client.get_token(request_body=data.clear_registration))
    if clearing is False:
        logging.warning("\nAn error occured while clearing registration user\n")
    


def test_login_happy_flow(auth_client, endpoints, data):
    registered_user_is_exist = auth_client.create_user(request_body=data.registration_data_for_test_login)

    if registered_user_is_exist is False:
        logging.warning(f"\nAn error occured while creating user to test login\n")
        raise

    response = auth_client.send_request(
        method = "POST",
        url = f"{endpoints.base_url}{endpoints.endpoint_users_login}",
        json = data.login_happy_flow
    )
    auth_client.check_status_code(response=response, expected_status=200)