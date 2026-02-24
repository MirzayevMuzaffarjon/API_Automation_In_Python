import pytest, logging
from api_test.api_cliets.API_Client import Client
from api_test.api_cliets.Auth_Cliend import AuthClient
from api_test.configs.Configurations import Endpoints
from api_test.data.Data_For_tests import Data


@pytest.fixture(scope='session')
def client():
    return Client()

@pytest.fixture(scope='session')
def auth_client():
    return AuthClient()

@pytest.fixture(scope='session')
def endpoints():
    return Endpoints()

@pytest.fixture(scope='session')
def data():
    return Data()