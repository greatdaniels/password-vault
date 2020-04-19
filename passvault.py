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