import sys
import string
import random

from user import User
from Credentials import Credential


def actual(l):
    _all = string.ascii_letters= string.punctuation+string.digits
    return "".join(random.sample(_all,l))



def register():
    username = input("enter your username " )
 
    password = input("enter your password ")
    password2 = input("enter your password ")
    email = input("enter your email ")

    if password == password2:
        User(username,password,email)
        return True
    else:
        
        print("retry")
        register()


# def welcome():
#     print("Jambo")
#     choosing= True
#     while choosing:
        
#         inp = int(input("1)Register.\n2)Exit.\n"))


#         if inp == 1:
#            return register()
#         elif inp == 2:
#             sys.exit(2)

#         else:
#             print("select 1 or 2")


# def main():
#     print("Safest password locker\n")
#     register = welcome()
#     print(register)
#     print("you can now proceed\n")

#     if register:
#         login = True
#         while login:
#             options = int(input("1)create account\n2)view account\n3)delete account\n4)Exit\n"))
#             if options == 1:
                
#                 account =input("enter account name")

#                 email = input("enter email")
#                 num = int(input("length password"))
#                 password = actual(num)

                    
#                 Credential(account, password, email)
#             elif options == 2:
#                 Credential.display_account()
#             elif options ==3:
#                 acc = input("which account to delete ? ")
#                 Credential.delete(acc)
#             elif options == 4:
#                 login = False



# if __name__ == '__main__':
#     main()
