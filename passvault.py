import random
import string
class User:
    """
    class that generates new instance of users
    """
    user_list = []

    def __init__(self, username, password):
        """
        method that defines properties of class user
        """
        self.username = username
        self.password = password

    def save_user(self):
        '''
        method that saves new user to user list
        '''
        User.user_list.append(self)

    @classmethod
    def display_user(cls):
        return cls.user_list

    @classmethod
    def verify_user(cls,username, password):
        """
        method to verify whether the user is in our user_list or not
        """
        a_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                    a_user == user.username
        return a_user


class Credentials():
    """
    class that generates new credentials instance
    """
    credentials_list = []

    def __init__(self, account, username, password):
        '''
        method that defines properties if class Credentials
        '''
        self.account = account
        self.username = username
        self.password = password

    def save_credential(self):
        '''
        method that saves a credential to credentials list
        '''
        Credentials.credentials_list.append(self)

    def delete_credential(self):
        '''
        method that deletes a credential from credentials list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_account(cls, account):
        '''
        method that takes in account name and returns credential that matches that account name
        '''
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential 

    @classmethod
    def credential_exists(cls, account):
        '''
        method that checks whether a credential exists in credential list
        Args:
            account: Account name to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns all items in credentials list
        '''
        return cls.credentials_list

        def generatePass(stringLen = 8):
            '''
            generating a random password
            '''
            password = string.ascii_uppercase + string.ascii_lowercase + string.digits + '~!@#$%^&*'
            return ''.join(random.choice(password) for i in range(stringLen))
        