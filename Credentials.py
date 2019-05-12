class Credential:
    credential_list = []

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        Credential.credential_list.append({"username":self.username,"password":self.password, "email":self.email})
    

    
    def generate_password():
        '''
        generate new password
        '''
        chars = '1234567890abcdefghijklmnopqrstuvwx123456789?/@-' #characters to choose from
        length = int(input("Enter the length of password you want: "))
        password = ''
        for chars in range(length):
            password += random.choice(chars) #generate random password
        print (password)

    # @classmethod
    # def display_account(cls):
    #     print("###   username   ##  password  ##   email  ###")
    #     for i in cls.credential_list:
    #         print(f" ### {i['username']} ## {i['password']} ## {i['email']} ###")
    # def search_account():
    #     pass

    # @classmethod
    # def delete(cls, acc):
    #     for i in cls.credential_list:
    #         if i['username'] == acc:
    #             print(f" you are about to delete {i['username']} account.")
    #             cls.credential_list.remove(i)


    # @classmethod
    # def view(cls):
    #     print("all your accounts")
    #     for i in cls.credential_list:
    #         print(f" || {i['username']} || {i['password']} || {i['email']}")
