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
        Comment.query.delete()
        
    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.title,"Youre testing")
        self.assertEquals(self.new_comment.user,self.user_James)
        self.assertEquals(self.new_comment.post,self.new_post)


    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)