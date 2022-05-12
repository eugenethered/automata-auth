import unittest

from cache.holder.RedisCacheHolder import RedisCacheHolder

from auth.repository.AuthRepository import AuthRepository


class AuthRepositoryTestCase(unittest.TestCase):

    def setUp(self) -> None:
        options = {
            'REDIS_SERVER_ADDRESS': '192.168.1.90',
            'REDIS_SERVER_PORT': 6379,
            'AUTH_INFO_KEY': 'test:auth:info'
        }
        self.cache = RedisCacheHolder(options)
        self.repository = AuthRepository(options)

    def tearDown(self):
        self.cache.delete('test:auth:info')

    def test_should_store_and_retrieve_auth_info(self):
        auth_info = {'API_KEY': 'X!X'}
        self.repository.store(auth_info)
        stored_auth_info = self.repository.retrieve()
        self.assertEqual(auth_info, stored_auth_info)


if __name__ == '__main__':
    unittest.main()
