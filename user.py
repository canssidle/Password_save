user_createaccount = []# Empty user_create account


class User:

    def __init__(self,username,password,email):
        """
        created insatances of the user class
        """
        self.username = username
        self.email = email
        self.password = password
        User.user = {"username":self.username, "email":self.email, "password":self.password}


    @classmethod
    def return_user(cls):
        return cls.user

   