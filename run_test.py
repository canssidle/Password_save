import unittest #importing the unittest module
from user import User #importing the user class

class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the contact class behaviours
    """
    def tearDown(self):
        """
        does clean up after each test case has run
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

    def test_save_account(self):
        """
        to check if the the new user is saved
        """
        self.new_user.save_account()#saving the new user
        self.assertEqual(len(User.user_createaccount),1)

    def test_login(self):
        """
        to check if the user can login
        """

        self.new_user.save_account()
        login = User("Canssidle","me2017","canssidlewairimu@gmail.com")
        login.save_account()  

    def test_generate_password(self):
        """
        test  to check if password is being generated
        """
        self.new_user.generate_password()
        self.assertEqual(self.new_user.password,"password")


    



        

if __name__ == '__main__':
    unittest.main()