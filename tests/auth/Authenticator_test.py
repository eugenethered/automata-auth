import unittest

from tests.helper.AuthenticatorHelper import AuthenticatorHelper


class AuthenticatorTestCase(unittest.TestCase):

    def setUp(self) -> None:
        options = {
            'AUTH_URL': 'https://some.auth/url/and/options',
        }
        self.authenticator = AuthenticatorHelper(options)
        self.authenticator.repository.store({'KEY': 'aaa', 'SECRET': 'bbb'})

    def test_should_have_auth_url(self):
        self.assertEqual(self.authenticator.auth_url, 'https://some.auth/url/and/options')

    def test_should_obtain_auth_value(self):
        result = self.authenticator.obtain_auth_value('KEY')
        self.assertEqual(result, 'aaa')


if __name__ == '__main__':
    unittest.main()
