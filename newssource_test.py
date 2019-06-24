import unittest 
from app.models import Source
class SourceTest(unittest.TestCase):
    '''
    Test of the class to test its behaviour
    '''
    def setUp(self):
        '''
        Setup method that runs before every test
        '''
        self.new_source = Source('ABC News','Best leading source','www.abcnews.com')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))
if __name__== '__main__':
    unittest.main()