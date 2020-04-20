import unittest
from passvault import User
from passvault import Credentials

class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for class User
    """

    def setUp(self):
        '''
        set up method to run before each user test case
        '''
        self.new_user = User('Dan','d3A1n7')

    def tearDown(self):
        '''
        method that cleans up after each test
        '''
        User.user_list = []

    def test_init(self):
        '''
        test case to check if user object is initialized correctly
        '''
        self.assertEqual(self.new_user.username,'Dan')
        self.assertEqual(self.new_user.password,'d3A1n7')

    def test_save_user(self):
        '''
        test case to check whether new user has been saved to user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_find_user(self):

        self.new_user.save_user()
        test_user = User("Kim", "k0E0y7")
        test_user.save_user()

        found_user = User.verify_user("Kim", "k0E0y7")
        self.assertEqual(found_user.username, test_user.username)
        self.assertEqual(found_user.password, test_user.password)

class TestCredentials(unittest.TestCase):
    """
    Test class that defines test cases for class Credentials
    """

    def setUp(self):
       '''
       method that runs before each Credentials test case
       '''
       self.new_credential = Credentials('Instagram','Dan','b3O1y6') 

    def tearDown(self):
        '''
        method that cleans up after each test
        '''
        Credentials.credentials_list = []

    def test_init(self):
        '''
        test case to check whether new instance of credentials has been initialized properly
        '''
        self.assertEqual(self.new_credential.account,'Instagram')
        self.assertEqual(self.new_credential.username,'Dan')
        self.assertEqual(self.new_credential.password,'b3O1y6') 

    def test_save_credential(self):
        '''
        test case to check whether new credential object has been saved to credentials list
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_credentials(self):
        '''
        test to check if we can save multiple credentials objects in the credentials list
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("Gmail", "greatdaniels", "k0E0y7")
        test_credential.save_credential()
        self.assertEqual(len(Credentials.credentials_list),2)
    def test_delete_credential(self):
        '''
        test to check whether we can delete a credential from our credentials list
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("Gmail", "greatdaniels", "k0E0y7")
        test_credential.save_credential()
        self.new_credential.delete_credential()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credential(self):
        '''
        test to check whether we can find a credential by account name and display information
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("Gmail", "greatdaniels", "k0E0y7")
        test_credential.save_credential()

        found_credential = Credentials.find_by_account("Gmail")
        self.assertEqual(found_credential.account, test_credential.account)

    def test_credential_exists(self):
        '''
        test to check if we can return a boolean if we cannot find a credential
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("Gmail", "greatdaniels", "k0E0y7")
        test_credential.save_credential()

        credential_exists = Credentials.credential_exists('Gmail')
        self.assertTrue(credential_exists)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all saved credentials
        '''
        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)

if __name__ == '__main__':
    unittest.main()