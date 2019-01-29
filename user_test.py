import unittest
from user import User

class TestUser(unittest.TestCase):
    """
    This is a class that will contain all tests for the user class
    """
    def setUp(self):
        """
        this will create new user before each test
        """
        self.new_user("kelvin","6980")

    def test_init(self):
        """
        This will test whetherthe user is registered correctly
        """
        self.assertEquall(self.new_user.login,"kelvin")
        self.assertEquall(self.new_user.password,"6980")

    def test_user_password(self):
        """
        this will test whether the user exist
        """
        self.assertTrue(User.user_exists)

    if_name_ == "_main_":
    unittest.main()        
