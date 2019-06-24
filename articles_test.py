import unittest
from app.models import Article
class ArticleTest(unittest.TestCase):
    '''
    Test Class to test its behaviour
    '''
    def setUp(self):
        '''
        Set up method that will run before test
        '''
        self.new_article = Article()
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))
if __name__ == '__main__':
    unittest.main()
    