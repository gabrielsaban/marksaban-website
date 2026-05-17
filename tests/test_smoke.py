import unittest
from xml.etree import ElementTree

from app import app


class SiteSmokeTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_pages_render(self):
        for path in ("/", "/contact", "/psychotherapy", "/resources"):
            with self.subTest(path=path):
                response = self.client.get(path)
                try:
                    self.assertEqual(response.status_code, 200)
                    self.assertIn(b"Mark Saban", response.data)
                finally:
                    response.close()

    def test_legacy_urls_redirect_to_canonical_pages(self):
        redirects = {
            "/index.html": "/",
            "/contact.html": "/contact",
            "/psychotherapy.html": "/psychotherapy",
            "/links.html": "/resources",
        }
        for path, location in redirects.items():
            with self.subTest(path=path):
                response = self.client.get(path)
                try:
                    self.assertEqual(response.status_code, 301)
                    self.assertEqual(response.headers["Location"], location)
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
            sitemap = ElementTree.fromstring(response.data)
            body = response.data.decode()
            self.assertIn("https://marksaban.co.uk/resources", body)
            self.assertNotIn("index.html", body)
            self.assertEqual(sitemap.tag, "{http://www.sitemaps.org/schemas/sitemap/0.9}urlset")
        finally:
            response.close()


if __name__ == "__main__":
    unittest.main()
