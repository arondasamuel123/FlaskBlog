from . import  main
from flask import render_template, url_for,redirect
from app.models import Posts, User
from flask_login import current_user, login_required
from .forms import PostForm
@main.route('/')
def home():
    posts = Posts.query.all()
    return render_template('home.html', posts=posts)

@main.route('/writer')
def writer():
    posts = Posts.query.all()
    return render_template('writer.html',posts=posts)

@main.route('/create', methods=['GET','POST'])
@login_required
def create_post():
    post_form = PostForm()
    user = current_user
    
    if user.user_type=='Writer':
        if post_form.validate_on_submit():
            post = Posts(title=post_form.title.data, category=post_form.category.data, blog=post_form.post.data,user=current_user)
            post.save_post()
            return redirect(url_for('main.writer'))
    else:
        return "This page is for only writers"
        
    return render_template('createpost.html', post_form=post_form)

# @main.route('post/<int:id>')
# def get_post(id):
#     post = Posts.query.filter_by(id=id).all()
    
#     return render_template('viewpost.html', post=post)
    
        
            

    