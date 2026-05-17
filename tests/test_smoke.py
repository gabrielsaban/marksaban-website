import unittest
from xml.etree import ElementTree

from app import app


class SiteSmokeTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_pages_render(self):
        for path in ("/", "/contact.html", "/psychotherapy.html", "/links.html"):
            with self.subTest(path=path):
                response = self.client.get(path)
                try:
                    self.assertEqual(response.status_code, 200)
                    self.assertIn(b"Mark Saban", response.data)
                finally:
                    response.close()

    def test_public_files_render(self):
        for path in ("/robots.txt", "/sitemap.xml", "/favicon.ico"):
            with self.subTest(path=path):
                response = self.client.get(path)
                try:
                    self.assertEqual(response.status_code, 200)
                finally:
                    response.close()

    def test_sitemap_is_valid_xml(self):
        response = self.client.get("/sitemap.xml")
        try:
            ElementTree.fromstring(response.data)
        finally:
            response.close()


if __name__ == "__main__":
    unittest.main()
