#!/usr/bin/env python3.6
from passvault import User, Credentials

def create_new_user(username, password):
    '''
    function to create a new user
    '''
    new_user = User(username, password)
    return new_user

def save_user(user):
    '''
    function to save a new user
    '''
    user.save_user()

def display_user():
    '''
    function to display existing user
    '''
    return User.display_user()

def login_user(username, password):
    '''
    function to check existence of user and login
    '''
    check_user = User.verify_user(username,password)
    return check_user

#Credentials functions definition

def create_new_credential(account, username, password):
    '''
    function to create new credentials
    '''
    new_credential = Credentials(account, username, password)
    return new_credential

def save_credential(credential):
    '''
    function to save credential
    '''
    credential.save_credential()

def delete_credential(credential):
    '''
    function to delete credential
    '''
    credential.delete_credential()

def display_credential():
    '''
    function to display credential
    '''
    return Credentials.display_credentials()

def find_credential(account):
    '''
    function that finds credential by account name
    '''
    return Credentials.find_by_account(account)

def check_credentials(account):
    '''
    function that checks whether a credential exists and returns boolean
    '''
    return Credentials.credential_exists(account)

def generate_password():
    '''
    function that generates random password
    '''
    auto_pass = Credentials.generatePass()
    return auto_pass


def passvault():
    print("\n Welcome to the Password VAULT... ")

    print('\n')
    while True:
        print("Enter one of the following to proceed: \n\n CA --> Create Account \n\n LI --> Login \n\n EX --> EXIT Application\n ")
        short_code = input('').lower().strip()
        if short_code == 'ca':
            print('\n')
            print('Sign Up \n')
            print('*' * 49)
            print('\n')
            username = input("User_name: ")
            print('\n')
            while True:
                print('Enter one of the following options to proceed:\n')
                
                print("TP --> To enter your password... \n\nGP --> To generate password...\n")
                password_select = input().lower().strip()
                if password_select == 'tp':
                    print('\n')
                    password = input("Enter Password:")
                    break
                elif password_select == 'gp':
                    password = generate_password()
                    break
                else:
                    print("\nInvalid entry... Please try again...\n")

            save_user(create_new_user(username, password))
            print('\n')
            print('-' * 90)
            print(f"Hello {username}, the account has been created successfully. Your password is : {password} ")
            print("-" * 90)
            print('\n')

        elif short_code == 'ex':
            print('-' * 70)
            print("Thank you for using passwords vault.. See you next time!")
            print('\n')
            break

        elif short_code == "li":
            print("*" * 49)
            print("Enter username and password")
            print("*" * 49)
            print('\n')
            username = input("User name : ")
            print('\n')
            password = input("Password : ")
            user_exists = login_user(username,password)
            print('\n')
            if user_exists == username:
                print(f"Hello {username}.Welcome To PassWord Vault")  
                print('\n')

                while True:
                    print("Use these short codes:\n\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n GP - Generate A randomn password \n D - Delete credential \n EX - Exit Session \n")
                    short_code = input().lower().strip()

                    if short_code == "cc":
                        print('\n')
                        print("Create New Credential")
                        print("."*20)
                        print('\n')
                        print("Account name:\n")
                        account = input().lower()
                        print('\n')
                        print("Your Account username:\n")
                        userName = input()
                        print('\n')
                        while True:
                            print(" TP - To type your own pasword if you already have an account:\n\n GP - To generate random Password")
                            print('\n')
                            password_Choice = input().lower().strip()
                            if password_Choice == 'tp':
                                print('\n')
                                password = input("Enter Your Own Password\n")
                                break
                            elif password_Choice == 'gp':
                                password = generate_password()
                                break
                            else:
                                print("\nInvalid Entry... Please try again...\n")
                        save_credential(create_new_credential(account,userName,password))
                        print('\n')
                        print(f"Account Credential for: {account} - UserName: {userName} - Password: {password} created succesfully")
                        print('\n')

                    elif short_code == "dc":
                        if display_credential():
                            print('-' * 50)
                            print("Here's your list of acoounts: ")
                            
                            print('*' * 30)
                            print('_'* 30)
                            for credential in display_credential():
                                print(f" \nAccount:{credential.account} \n User Name:{credential.username}\n Password:{credential.password}")
                                print('_'* 30)
                            print('*' * 30)
                        else:
                            print("\nYou don't have any credentials saved yet...\n")

                    elif short_code == "fc":
                        print('-' * 50)
                        print("Enter the Account Name you want to search")
                        print('\n')
                        search_name = input().lower()
                        if find_credential(search_name):
                            search_credential = find_credential(search_name)
                            print(f"\n Account Name : {search_credential.account}")
                            print('-' * 50)
                            print(f"User Name: {search_credential.username} Password :{search_credential.password}")
                            print('-' * 50)
                        else:
                            print("\nThat Credential does not exist...\n")

                    elif short_code == "d":
                        print("\nEnter the account name of the Credentials you want to delete: \n")
                        search_name = input().lower()
                        if find_credential(search_name):
                            search_credential = find_credential(search_name)
                            print("_"*50)
                            search_credential.delete_credential()
                            print('\n')
                            print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                            print('\n')
                        else:
                            print("\nThat Credential you want to delete does not exist in your vault...\n")

                    elif short_code == 'gp':
                        password = generate_password()
                        print('-' * 50)
                        print(f"Password: {password} Has been generated succesfully...")
                        print('-' * 50)
                        print('\n')
                    
                    elif short_code == 'ex':
                        print('-' * 50)
                        print("Logged out of current session \n")
                        break
                    else:
                        print("\n Wrong entry... Check your entry again and let it match those in the menu \n")
                # else:
                #     print("Please enter a valid input to continue")

            else:
                print("\nInvalid username or password...\n")

        else:
            print('\nInvalid Entry...\n') 

if __name__ == '__main__':
    passvault()
