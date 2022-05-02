import unittest 
from app.models import Article  

class ArticlesTest(unittest.TestCase):
    '''
    Test to define Article class behavior
    '''
    def setUp(self):
        '''
        Method to run before every test 
        '''
        self.new_article = Article('Isaac Ndirangu & Sheina hamisi', 'Trending news about gender equality and gender based violence', '2022-04-02T05:09:17Z', 'https://eige.europa.eu/gender-based-violence/what-is-gender-based-violence', 'https://images.unsplash.com/photo-1645389776061-01e3b6414546?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60', 'Gender equality')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Article))

if __name__ == '__main__':
    unittest.main()