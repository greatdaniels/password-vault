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

    
        
