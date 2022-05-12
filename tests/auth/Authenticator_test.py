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

    def test_should_get_timestamp(self):
        timestamp = self.authenticator.get_timestamp()
        self.assertGreater(timestamp, 1)

    def test_should_sign_value_with_secret(self):
        secret = 'hat'
        value = 'rabbit'
        result = self.authenticator.sign_secret_value(secret, value)
        self.assertEqual(result, 'ef71c2d73728d402f8fc813f7bfa128db5b5f68166f25b89c3a901922b5704a2')


if __name__ == '__main__':
    unittest.main()
