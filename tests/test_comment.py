import unittest
from app.models import Comment,User,Posts

class CommentModelTest(unittest.TestCase):
    """
    """
    
    def setUp(self):
        self.user_made = User(username = 'jack', password= 'pass', email= 'jack@devops.com')
        self.new_post = Posts(title='Python', blog='Python is awesome',category="flask" ,user=self.user_made)
        self.new_comment = Posts( comment='Great posts',post = self.new_post, user=self.user_made)
    def tearDown(self):
        Posts.query.delete()
        User.query.delete()
        
    def test_check_instance_variables(self):
        self.assertEquals(self.new_post.title,"Youre testing")
        self.assertEquals(self.new_post.blog,"This is the test of the century")
        self.assertEquals(self.new_post.category,"my-thoughts")
        self.assertEquals(self.new_post.user,self.user_James)


    def test_save_post(self):
        self.new_review.save_review()
        self.assertTrue(len(Posts.query.all())>0)