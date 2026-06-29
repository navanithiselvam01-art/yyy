import unittest
from app import app

class FlaskApplicationTest(unittest.TestCase):

    def setUp(self):
        application.testing = True
        self.client = application.test_client()

    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_content(self):
        response = self.client.get("/")
        self.assertIn(b"TechNova Solutions", response.data)

    def test_content_type(self):
        response = self.client.get("/")
        self.assertEqual(response.content_type, "text/html; charset=utf-8")

if __name__ == "__main__":
    unittest.main()
