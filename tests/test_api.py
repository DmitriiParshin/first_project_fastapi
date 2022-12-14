from unittest import TestCase
from fastapi.testclient import TestClient

from app.main import app as web_app


class APITestCase(TestCase):

    def setUp(self):
        self.client = TestClient(web_app)

    def test_main_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)

    def test_create_user(self):
        user_data = {
            'user_form': {
                'email': 'user123@mail.ru',
                'password': 'user7',
                'first_name': 'qwe',
                'last_name': 'rty',
                'nickname': 'yui'
            }
        }

        response = self.client.post('/user', json=user_data)
        self.assertEqual(response.status_code, 200)
