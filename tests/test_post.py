import unittest
from app.models import Posts, User


class PostsModelTest(unittest.TestCase):
    """
    """
    def setUp(self):
        self.user_James = User(username = 'james', password= 'pass', email= 'abcdef@email.com')
        self.new_post = Posts(title="You're testing", blog='This the test of the century',category="my-thoughts" ,user=self.user_James)
    def tearDown(self):
        Posts.query.delete()
        User.query.delete()
        
    def test_check_instance_variables(self):
        self.assertEquals(self.new_post.title,"Youre testing")
        self.assertEquals(self.new_post.blog,"This is the test of the century")
        self.assertEquals(self.new_post.category,"my-thoughts")
        self.assertEquals(self.new_post.user,self.user_James)


    def test_save_post(self):
        self.new_post.save_post()
        self.assertTrue(len(Posts.query.all())>0)