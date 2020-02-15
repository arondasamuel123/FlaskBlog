from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin
from . import login_manager

class User(db.Model,UserMixin):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    pass_secure = db.Column(db.String(255))
    user_type = db.Column(db.String(255))
    posts = db.relationship('Posts',backref='user', lazy='dynamic')
    comments = db.relationship('Comment', backref='user', lazy='dynamic')
    
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
        
   
    def set_password(self, password):
        self.pass_secure = generate_password_hash(password)
    def verify_password(self,password):
        return check_password_hash(self.pass_secure, password)
    
    def save_user(self):
        db.session.add(self)
        db.session.commit()
    
    
    
class Posts(db.Model):
    __tablename__='posts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    blog = db.Column(db.String(255))
    category = db.Column(db.String(255))
    blog_created = db.Column(db.DateTime,default=datetime.utcnow)
    comments = db.relationship('Comment', backref='post', lazy='dynamic')

class Comment(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    comment = db.Column(db.String(255))