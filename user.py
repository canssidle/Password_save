user_createaccount = []# Empty user_create account


class User:

    def __init__(self,username,password,email):
        """
        created insatances of the user class
        """

    def save_account(self):
        """
        save_account saves user objects into user_create account
        """
        User.user_createaccount.append(self)



        #Test the credentials class
