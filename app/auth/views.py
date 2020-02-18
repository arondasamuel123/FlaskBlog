from . import auth
from app.models import User
from .forms import RegistrationForm,LoginForm
from .. import db
from flask import render_template, url_for,redirect,flash
from flask_login import login_user, logout_user



@auth.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, pass_secure=form.password.data,user_type=form.role.data)
        user.set_password(form.password.data)
        user.save_user()
        return "User has been created"
        
    return render_template('auth/register.html', registration_form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        
        if user.user_type=='Writer' and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(url_for('main.writer'))
        elif user.user_type =='User' and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(url_for('main.home'))
    flash('Invalid Username or Password')
    return render_template('auth/login.html', login_form=login_form)
            
@auth.route('/logout')
def logout():
    logout_user()
    
    return redirect(url_for('main.home'))
    
        


  
    