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

