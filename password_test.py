import unittest #importing unittest module
from password import password #importing password class

class TestPassword(unittest.TestCase):
    """
    Here is where we will perfome all our test
    """
    def setUp(self):
        """
        This function will create a new instance password before each test
        """
        self.new_password =password("slack","Adeu","0713")

    def tearDown(self):
        """
        Here will be clearing password after every test to avoid confusion
        """
        Password.password = []

    def test_new_pass(self):
        """
        Here will test if a new password is initiated correctly
        """
        self.assertEquall(self.new_password.account,"slack")
        self.assertEquall(self.new_password.username,"Adeu")
        self.assertEquall(self.new_password.password,"0713")
        
