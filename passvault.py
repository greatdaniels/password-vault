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
        method that saves new credential to credentials list
        '''
        Credentials.credentials_list.append(self)
        