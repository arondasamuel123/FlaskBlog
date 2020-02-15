from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from datatime import datatime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    pass_secure = db.Column(db.String(255))
    posts = db.relationship('Posts',backref='user', lazy='dynamic')
    comments = db.relationship('Comment', backref='user', lazy='dynamic')
    
    
    @property
    def password(self):
        return self.pass_secure
    
    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)
    def verify_password(self,password):
        return check_password_hash(self.pass_secure, password)
    
    
    
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    blog = db.Column(db.String(255))
    blog_created = db.Column(db.DateTime,default=datatime.utcnow)
    

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))