from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField,BooleanField
from wtforms.validators import Required,Email, EqualTo
from ..models import User
from wtforms import ValidationError


class RegistrationForm(FlaskForm):
    email = StringField('Enter Email Address', validators=[Required(), Email()]) 
    username = StringField('Enter your username',validators=[Required()])
    password = PasswordField('Enter your password', validators=[Required(),EqualTo('password_confirm')])
    password_confirm = PasswordField('Confirm password',validators=[Required()])
    role = SelectField(u'Select your role', choices=[('User', 'user'),('Writer', 'writer') ], validators=[Required()])
    submit = SubmitField('Sign Up')
    
    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError("There is already an account with this email")
    def validate_username(self, data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError("This username is already taken")
        
class LoginForm(FlaskForm):
    email = StringField('Enter Email Address', validators=[Required(), Email()])
    password = PasswordField('Enter your password', validators=[Required()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
        
        