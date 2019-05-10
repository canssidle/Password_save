import unittest
from user import User

class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the contact class behaviours
    """

    def setUp(self):
        """
        self is a placeholder for an instance
        """

        self.new_user = User("Canssidle","me2017","canssidlewairimu@gmail.com")
        """
        This is the user object
        """
    def test_init(self):
        """
        This is to check if an object is initialized properly
        """
        self.assertEqual(self.new_user.username,"canssidle")
        self.assertEqual(self.new_user.password,"me2017")
        self.assertEqual(self.new_user.email,"cansssidlewairim@gmail.com")

    def test_save_user(self)

if __name__ == '__main__':
    unittest.main()