import website
import unittest
import database

class WebsiteTests(unittest.TestCase):

    def setUp(self):
        website.app.testing = True
        self.app = website.app.test_client()

    def test_index(self):
        result = self.app.get('/')
        self.assertIsNotNone(result)
    
    def test_device(self):
        result = self.app.get('/device')
        self.assertIsNotNone(result)

    def test_list(self):
        result = self.app.get('/list')
        self.assertIsNotNone(result)
        
class DatabaseTest(unittest.TestCase):

    def test_computerRead(self):
        result = database.getComputerHighScore('cpu')
        self.assertNotEqual(result, '')
        
    def test_laptopRead(self):
        result = database.getLaptopHighScore('display')
        self.assertNotEqual(result, '')
            
    def test_connect(self):
        result = database.connectDB()
        self.assertIsNotNone(result)

