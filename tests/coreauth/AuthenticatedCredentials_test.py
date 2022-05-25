import unittest

from tests.helper.AuthenticatedCredentialsHelper import AuthenticatedCredentialsHelper


class AuthenticatedCredentialsTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.authenticator = AuthenticatedCredentialsHelper()
        self.authenticator.repository.store({'KEY': 'aaa', 'SECRET': 'bbb'})

    def test_should_obtain_auth_value(self):
        sought_key = self.authenticator.obtain_auth_value('KEY')
        self.assertEqual(sought_key, 'aaa')
        sought_secret = self.authenticator.obtain_auth_value('SECRET')
        self.assertEqual(sought_secret, 'bbb')


if __name__ == '__main__':
    unittest.main()
