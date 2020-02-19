from . import  main
from flask import render_template, url_for,redirect
from app.models import Posts, User, Comment
from flask_login import current_user, login_required
from .forms import PostForm, CommentForm, UpdateBlogForm
from .. import db
from sqlalchemy import desc
from ..requests import get_quotes
from ..email import mail_message
@main.route('/')
def home():
    posts = Posts.query.order_by(Posts.blog_created.desc()).all()
    quote = get_quotes()
    user = current_user
    if user.user_type=='User':
        return render_template('home.html', posts=posts, quote=quote)
    else:
        return render_template('notuser.html')

@main.route('/writer')
def writer():
    posts = Posts.query.order_by(Posts.blog_created.desc()).all()
    user = current_user
    if user.user_type=='Writer':
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
            users = User.query.filter_by(user_type='User').all()
            for user in users:
                mail_message("New Post has arrived", "email/new_post", user.email, user=user)
            return redirect(url_for('main.writer'))
    else:
        return "This page is for only writers"
        
    return render_template('createpost.html', post_form=post_form)

@main.route('/post/<int:id>')
def get_post(id):
    post = Posts.query.filter_by(id=id).all()
    
    return render_template('viewpost.html', post=post)
@main.route('/createcomment/<int:id>', methods=['GET', 'POST'])
@login_required
def create_comment(id):
    comment_post = Posts.query.get(id)
    user = current_user
    comment_form = CommentForm()
    
    if user.user_type=='User':
        if comment_form.validate_on_submit():
            new_comment = Comment(comment=comment_form.comment.data, user=current_user, post=comment_post)
            new_comment.save_comment()
            
            return "Comment added"
    else:
            return "This page is for only users"
    return render_template('addcomment.html', comment_form=comment_form)

@main.route('/viewcomments/<int:id>')
def get_comments(id):
    
    comments = Comment.query.filter_by(post_id=id).all()
    
    return render_template('viewcomment.html', comments=comments)


@main.route('/dblog/<int:id>', methods=['GET', 'POST'])
def delete_blog(id):
    
    delete_post = Posts.query.filter_by(id=id).first()
    db.session.delete(delete_post)
    db.session.commit()
    
    return redirect(url_for('main.writer'))

    # return "Post Deleted"
    
@main.route('/ublog/<int:id>', methods=['GET', 'POST'])
def update_blog(id):
    blog_update = Posts.query.filter_by(id=id).first()
    update_form = UpdateBlogForm()
    if update_form.validate_on_submit():
        blog_update.title = update_form.title.data
        blog_update.blog = update_form.post.data
        blog_update.category = update_form.category.data
        
        db.session.add(blog_update)
        db.session.commit()
        return "Blog updated"
    
    return render_template("update.html", update_form=update_form)

@main.route('/dcomment/<int:id>', methods=['GET', 'POST'])
def delete_comment(id):
    delete_comm = Comment.query.filter_by(id=id).first()
    db.session.delete(delete_comm)
    db.session.commit()
    
    return redirect(url_for('main.writer'))

        
    
        
            

    