import unittest

from cache.holder.RedisCacheHolder import RedisCacheHolder

from coreauth.repository.AuthRepository import AuthRepository


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
        auth_info = {'AUTH_TOKEN': 'X!X'}
        self.repository.store(auth_info)
        stored_auth_info = self.repository.retrieve()
        self.assertEqual(auth_info, stored_auth_info)

    def test_should_append_store_additional_auth_key(self):
        auth_info = {'AUTH_TOKEN': 'X!X'}
        self.repository.store(auth_info)
        stored_auth_info = self.repository.retrieve()
        self.assertEqual(auth_info, stored_auth_info)
        self.repository.append('OTHER', '22')
        auth_info = self.repository.retrieve()
        self.assertEqual(auth_info['AUTH_TOKEN'], 'X!X')
        self.assertEqual(auth_info['OTHER'], '22')

    def test_should_delete_value_from_stored_auth_info(self):
        auth_info = {'AUTH_TOKEN': 'X!X', 'OTHER': '22'}
        self.repository.store(auth_info)
        stored_auth_info = self.repository.retrieve()
        self.assertEqual(auth_info, stored_auth_info)
        self.repository.remove('OTHER')
        auth_info = self.repository.retrieve()
        self.assertEqual(len(auth_info), 1)
        self.assertFalse('OTHER' in auth_info)
        self.assertEqual(auth_info['AUTH_TOKEN'], 'X!X')

if __name__ == '__main__':
    unittest.main()
