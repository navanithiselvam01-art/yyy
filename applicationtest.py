import unittest
from app import app

class FlaskApplicationTest(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_content_type(self):
        response = self.client.get("/")
        self.assertIn("text/html", response.content_type)

    def test_home_page_content(self):
        response = self.client.get("/")
        self.assertIn(b"Hotel Management System", response.data)

if __name__ == "__main__":
    unittest.main()
