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
    print("Welcome to the Password Vault...\n\n Enter one of the following to proceed: \n\n CA --> Create Account \n\n LI --> Login ")
    short_code = input('').lower().strip()
    if short_code == 'ca':
        print('Sign Up')
        print('*' * 70)
        username = input("User_name: ")
        while True:
            print("TP --> To enter your password... \n\n GP --> To generate password...")
            password_select = input().lower().strip()
            if password_select == 'tp':
                password = input("Enter Password: \n")
                break
            elif password_select == 'gp':
                password = generate_password()
                break
            else:
                print("Invalid")

        save_user(create_new_user(username, password))
        print('*' * 90)
        print(f"Hello {username}, the account has been created successfully. Your password is : {password} ")
        print("*" * 90)

    elif short_code == "li":
        print("*" * 70)
        print("Enter username and password")
        print("*" * 70)
        username = input("User name : ")
        password = input("Password : ")
        login_user(username, password)
        if True:
            print(f"Hello {username}.Welcome To PassWord Vault")  
            print('\n')
        # else:
            #code to handle edge case

    while True:
        print("Use these short codes:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n GP - Generate A randomn password \n D - Delete credential \n EX - Exit the application \n")
        short_code = input().lower().strip()

        if short_code == "cc":
            print("Create New Credential")
            print("."*20)
            print("Account name ...")
            account = input().lower()
            print("Your Account username")
            userName = input()
            while True:
                print(" TP - To type your own pasword if you already have an account:\n GP - To generate random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    password = input("Enter Your Own Password\n")
                    break
                elif password_Choice == 'gp':
                    password = generate_password()
                    break
                else:
                    print("Invalid password please try again")
            save_credential(create_new_credential(account,userName,password))
            print('\n')
            print(f"Account Credential for: {account} - UserName: {userName} - Password:{password} created succesfully")
            print('\n')

        elif short_code == "dc":
            if display_credential():
                print("Here's your list of acoounts: ")
                 
                print('*' * 30)
                print('_'* 30)
                for account in display_credential():
                    print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                    print('_'* 30)
                print('*' * 30)
            else:
                print("You don't have any credentials saved yet..........")

        elif short_code == "fc":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print('-' * 50)
                print(f"User Name: {search_credential.userName} Password :{search_credential.password}")
                print('-' * 50)
            else:
                print("That Credential does not exist")
                print('\n')

        elif short_code == "d":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_"*50)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                print('\n')
            else:
                print("That Credential you want to delete does not exist in your store yet")
        
