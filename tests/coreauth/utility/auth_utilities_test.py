import unittest

from coreauth.utility.auth_utilities import get_timestamp, sign_value_with_secret


class AuthUtilitiesTestCase(unittest.TestCase):

    def test_should_get_timestamp(self):
        timestamp = get_timestamp()
        self.assertGreater(timestamp, 1)

    def test_should_sign_value_with_secret(self):
        secret = 'hat'
        value = 'rabbit'
        result = sign_value_with_secret(value, secret)
        self.assertEqual(result, 'ef71c2d73728d402f8fc813f7bfa128db5b5f68166f25b89c3a901922b5704a2')


if __name__ == '__main__':
    unittest.main()
