import os
from dotenv import load_dotenv

class Endpoints:
    load_dotenv()
    base_url = os.getenv("BASE_URL")
    endpoint_health_check = os.getenv("ENDPOINT_HEALTH_CHECK")
    endpoint_users_register = os.getenv("ENDPOINT_USERS_REGISTER")
    endpoint_users_login = os.getenv("ENDPOINT_USERS_LOGIN")
    endpoint_users_profile_get = os.getenv("ENDPOINT_USERS_PROFILE_GET")
    endpoint_users_profile_edit = os.getenv("ENDPOINT_USERS_PROFILE_EDIT")
    endpoint_users_profile_delete = os.getenv("ENDPOINT_USERS_PROFILE_DELETE")
    endpoint_users_log_out = os.getenv("ENDPOINT_USERS_LOG_OUT")
    endpoint_users_change_password = os.getenv("ENDPOINT_USERS_CHANGE_PASSWORD")
    endpoint_notes = os.getenv("ENDPOINT_NOTES")