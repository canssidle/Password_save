import unittest #importing the unittest module
import pyperclip
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


    #<---Test for the credentials--->#
    from user import credentials

class TestCredentials(unittest.TestCase):
    def setUp(self):

        self.user_credentials = Credentials("Canssidle","me2017","canssidlewairimu@gmail.com")

    def tearDown(self):
        CRedentials.user_credentials = []

    def test_init(self):
        self.assertEqual(self.user_credential.usernsme, "Canssidle")
        self.assertEqual(self.user_credential.password, "me2017")
        self.assertEqual(self.user_credential.email, "canssidlewairimu@gmail.com")
       
     def test_save_credentials(self):
        self.user_credential.save_credentials()
        self.assertEqual(len(Credentials.user_credentials), 1)

    def test_save_multiple_credentials(self):
        self.user_credential.save_credentials()
        test_Credentials = Credentials("username", "password", "email")
        test_Credentials.save_credentials()

        self.assertEqual(len(Credentials.user_credentials), 2)
    
    def test_delete_credentials(self):
        self.user_credential.save_credentials()
        test_Credentials = Credentials("username", "password", "email")
        test_Credentials.save_credentials()

        self.assertEqual(len(Credentials.user_credentials), 1)

    def test_display_credentials(self):
        self.assertEqual(Credentials.display_credentials(),Credentials.user_credentials)

    def test_find_account(self):
        self.user_credential.save_credentials()

        test_Credentials = Credentials("Canssidle", "me2017","canssidlewairimu@gmail.com" )
        test_Credentials.save_credentials()

        found_account = Credentials.find_by_username("Canssidle")

        self.assertEqual(found_account.email,test_Credentials.email)

    def test_copy_account(self):
        '''
        Test to confirm that we are copying a credential from the accounts found
        '''
        self.user_credential.save_credentials()
        Credentials.copy_credential("Canssidle")
    
        self.assertEqual(self.user_credential.password,pyperclip.paste())
    




        

if __name__ == '__main__':
    unittest.main()