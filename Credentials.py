class Credential:
    credential_list = []

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        Credential.credential_list.append({"username":self.username,"password":self.password, "email":self.email})
    
    

    @classmethod
    def display_account(cls):
        print("###   username   ##  password  ##   email  ###")
        for i in cls.credential_list:
            print(f" ### {i['username']} ## {i['password']} ## {i['email']} ###")

    @classmethod
    def search_account(cls,username):
        for i in cls.credential_list:
            if i['username'] == username:
                return username 

        

    @classmethod
    def delete(cls, acc):
        for i in cls.credential_list:
            if i['username'] == acc:
                print(f" you are about to delete {i['username']} account.")
                cls.credential_list.remove(i)


    @classmethod
    def view(cls):
        print("all your accounts")
        for i in cls.credential_list:
            print(f" || {i['username']} || {i['password']} || {i['email']}")

    @classmethod
    def copy_credential(cls,username):
        credential_found = Credentials.find_by_username(username)
        pyperclip.copy(credential_found.password)
        

