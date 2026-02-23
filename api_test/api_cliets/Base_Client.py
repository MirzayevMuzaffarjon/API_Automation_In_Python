import logging
import requests
from requests import RequestException
import pytest_check as check
from jsonschema import validate, ValidationError


class BaseClient:
    def __init__(self, session = None):
        self.session = session or requests.Session()

    def send_request(self, method, url, params=None, headers=None, json=None, data=None, files=None, timeout=None):
        #Logging all request data
        logging.info(f"\n---NEW REQUEST---\n")
        logging.info(f"\n---request method: {method}\n")
        logging.info(f"\n---request url: {url}\n")
        if params is not None: logging.info(f"\n---request params: \n{params}\n")
        if headers is not None: logging.info(f"\n---request headers: \n{headers}\n")
        if json is not None: logging.info(f"\n---request body: \n{json}\n")
        if data is not None: logging.info(f"\n---request data: \n{data}\n")
        if timeout is not None: logging.info(f"\n---request timeout: \n{timeout}\n")

        #Sending request
        try:
            response =  self.session.request(
                method = method,
                url = url,
                params = params,
                headers = headers,
                json = json,
                data = data,
                files=files,
                timeout = timeout
            )

            if response.status_code is not None: logging.info(f"\n---response status code: {response.status_code}\n")

            try:
                response_body = response.json()
                logging.info(f"\n---Response JSON: \n{response_body}\n")
            except ValueError:
                logging.info(f"\n---Response TEXT: \n{response.text}\n")

            logging.info(f"\n---response header: \n{response.headers}\n")

            return response

        except RequestException as e:
            logging.error(f"\n---Error type: {e.__class__.__name__} \nMessage: {e}\n")

    @staticmethod
    def check_status_code(response, expected_status):
        check.equal(response.status_code, expected_status,
                    f"---Unexpected status code!!! Expected: {expected_status}, got: {response.status_code}")

    @staticmethod
    def check_json_schema(actual_json, expected_json_schema):
        try:
            validate(instance=actual_json, schema=expected_json_schema)
        except ValidationError as e:
            check.is_true(False, f"---Schema validation error: {e.message}")

    @staticmethod
    def check_to_equality(element1, element2):
        check.equal(element1, element2, f"---{element1} is not equal to {element2}")