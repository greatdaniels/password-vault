import unittest
from passvault import User

class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for class User
    """

    def setUp(self):
        '''
        set up method to run before each test case
        '''
        self.new_user = User('Dan','d3A1n7')

    def test_init(self):
        '''
        test case to check if user object is initialized correctly
        '''
        self.assertEqual(self.new_user.username,'Dan')
        self.assertEqual(self.new_user.password,'d3A1n7')
        

if __name__ == '__main__':
    unittest.main()