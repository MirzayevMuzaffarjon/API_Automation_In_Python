import logging
from api_test.api_cliets.API_Client import Client
from api_test.data.Data_For_tests import Data
from api_test.configs.Configurations import Endpoints


class AuthClient(Client, Data, Endpoints):
    def __init__(self, session = None):
        super().__init__(session)

    def create_user(self, request_body):
        try:
            response = self.send_request(
                method="POST",
                url=f"{self.base_url}{self.endpoint_users_register}",
                json=request_body
            )
            response.raise_for_status()
            assert response.status_code == 201
            return True

        except Exception as e:
            logging.warning(f"\nFail create user while creating user: {e}")
            return False


    def get_token(self, request_body):
        try:
            response = self.send_request(
                method="POST",
                url=f"{self.base_url}{self.endpoint_users_login}",
                json=request_body
            )
            response.raise_for_status()
            assert response.status_code == 200

            return response.json()["data"]["token"]

        except Exception as e:
            logging.warning(f"\nAn error occurs while login. \nuser: {request_body} \nException: {e}")
            return False


    def delete_account(self, token):
        try:
            response = self.send_request(
                method="DELETE",
                url=f"{self.base_url}{self.endpoint_users_profile_delete}",
                headers={"x-auth-token": token, "Accept": "application/json"}
            )
            response.raise_for_status()
            assert response.status_code == 200
            return True

        except Exception as e:
            logging.warning(f"\nFail delete profile while clearing registration data: {e}")
            return False