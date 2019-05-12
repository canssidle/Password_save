class Credential:
    credential_list = []

    def __init__(self, account, password, email):
        self.account = account
        self.password = password
        self.email = email
        Credential.credential_list.append({"account":self.account,"password":self.password, "email":self.email})
    

    
    def generate_password():
        pass

    @classmethod
    def display_account(cls):
        print("###   account name   ##  password  ##   email  ###")
        for i in cls.credential_list:
            print(f" ### {i['account']} ## {i['password']} ## {i['email']} ###")
    def search_account():
        pass

    @classmethod
    def delete(cls, acc):
        for i in cls.credential_list:
            if i['account'] == acc:
                print(f" you are about to delete {i['account']} account.")
                cls.credential_list.remove(i)


    # @classmethod
    # def view(cls):
    #     print("all your accounts")
    #     for i in cls.credential_list:
    #         print(f" || {i['account']} || {i['password']} || {i['email']}")
