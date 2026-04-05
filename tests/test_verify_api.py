import unittest
import requests

class TestAPIEndpoints(unittest.TestCase):

    BASE_URL = 'http://your-api-url.com'

    def test_get_endpoint(self):
        response = requests.get(f'{self.BASE_URL}/endpoint')
        self.assertEqual(response.status_code, 200)
        self.assertIn('data', response.json())

    def test_post_endpoint(self):
        payload = {'key': 'value'}
        response = requests.post(f'{self.BASE_URL}/endpoint', json=payload)
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json())

    def test_put_endpoint(self):
        payload = {'key': 'new_value'}
        response = requests.put(f'{self.BASE_URL}/endpoint/1', json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['key'], 'new_value')

    def test_delete_endpoint(self):
        response = requests.delete(f'{self.BASE_URL}/endpoint/1')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()