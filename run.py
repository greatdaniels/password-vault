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