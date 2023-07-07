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
    
    def setUp(self):
        self.app = database.Database()
        
    def test_computerRead(self):
        result = self.app.getComputerHighScore('cpu')
        self.assertNotEqual(result, '')
        
    def test_laptopRead(self):
        result = self.app.getLaptopHighScore('display')
        self.assertNotEqual(result, '')
            
    def test_connect(self):
        result = self.app.connectDB()
        self.assertIsNotNone(result)

