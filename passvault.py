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