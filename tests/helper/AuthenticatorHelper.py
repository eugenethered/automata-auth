from coreauth.Authenticator import Authenticator, AUTH_URL
from coreauth.repository.AuthRepository import AuthRepository


class AuthenticatorHelper(Authenticator):

    def __init__(self, options):
        self.auth_url = options[AUTH_URL]
        self.repository = AuthRepositoryHelper()

    @staticmethod
    def should_update_url() -> bool:
        return True


class AuthRepositoryHelper(AuthRepository):

    def __init__(self):
        self.data = {}

    def store(self, auth_info):
        self.data = auth_info

    def retrieve(self):
        return self.data


