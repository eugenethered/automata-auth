from coreauth.AuthenticatedCredentials import AuthenticatedCredentials
from tests.helper.AuthenticatorHelper import AuthRepositoryHelper


class AuthenticatedCredentialsHelper(AuthenticatedCredentials):

    def __init__(self):
        self.repository = AuthRepositoryHelper()
