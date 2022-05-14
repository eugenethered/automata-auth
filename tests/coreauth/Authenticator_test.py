import unittest

from coreauth.exception.AuthenticatorError import AuthenticatorError
from tests.helper.AuthenticatorHelper import AuthenticatorHelper


class AuthenticatorTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.options = {
            'AUTH_URL': 'https://some.auth/url/and/options',
        }
        self.authenticator = AuthenticatorHelper(self.options)
        self.authenticator.repository.store({'KEY': 'aaa', 'SECRET': 'bbb'})

    def test_should_have_auth_url(self):
        self.assertEqual(self.authenticator.auth_url, 'https://some.auth/url/and/options')

    def test_should_obtain_auth_value(self):
        result = self.authenticator.obtain_auth_value('KEY')
        self.assertEqual(result, 'aaa')

    def test_should_raise_exception_when_update_url_has_not_been_set_and_should_update_url_indicated(self):
        should_update = self.authenticator.should_update_url()
        self.assertTrue(should_update)
        with self.assertRaises(AuthenticatorError):
            self.authenticator.update_url('some-url')

    def test_should_update_url(self):
        class CustomAuthenticator(AuthenticatorHelper):
            def update_url(self, url) -> str:
                return f'{url}-updated'
        authenticator = CustomAuthenticator(self.options)
        should_update = authenticator.should_update_url()
        self.assertTrue(should_update)
        updated_url = authenticator.update_url('some-url')
        self.assertEqual(updated_url, 'some-url-updated')


if __name__ == '__main__':
    unittest.main()
