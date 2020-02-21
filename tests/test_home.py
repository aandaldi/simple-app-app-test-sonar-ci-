from unittest import TestCase
from app import app


class BaseTest(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass


class TestHome(BaseTest):
    def test_index(self):
        with self.app as client:
            request = client.get('/index')
            expect = {
                "message": "Hello World"
            }

            self.assertEqual(200, request.status_code)

            self.assertEqual(expect, request.get_json())
            self.assertEqual('Hello World', request.get_json().get('message'))

    def test_list_item(self):
        with self.app as client:
            request = client.get('/item')
            expect = {
                "message": "This is Item"
            }

            self.assertEqual(200, request.status_code)

            self.assertEqual(expect, request.get_json())

