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

    def save_account(self):
        User.user_createaccount.append(self)
    
    def generate_password():
       pass
    @classmethod
    def return_user(cls):
        return cls.user

   