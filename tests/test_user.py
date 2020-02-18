import unittest
from app.models import User


class UserModelTest(unittest.TestCase):
    """
    Test class for User Model
    """
    
    def setUp(self):
        self.new_password = User (username='123456', email='qwert@hj.bn', password='123456')
        
    
    def test_password_setter(self):
        print(self.new_password.pass_secure)
        self.assertTrue(self.new_password.pass_secure)
        
    def test_no_access_password(self):
        self.assertRaises(AttributeError)
        
    def test_password_verification(self):
        self.assertTrue(self.new_password.verify_password('123456'))
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_password, User))