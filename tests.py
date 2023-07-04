import website
import unittest

class WebsiteTests(unittest.TestCase):

    def setUp(self):
        website.app.testing = True
        self.app = website.app.test_client()

    def test_index(self):
        result = self.app.get('/')
    
    def test_device(self):
        result = self.app.get('/device')

    def test_list(self):
        result = self.app.get('/list')

