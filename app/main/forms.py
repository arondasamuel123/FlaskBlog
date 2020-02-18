from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, TextAreaField,StringField
from ..models import Posts
from wtforms import ValidationError
from wtforms.validators import Required


class PostForm(FlaskForm):
    title = StringField('Enter your title', validators=[Required()])
    post = TextAreaField('Enter your post', validators=[Required()])
    category = SelectField(u'Category',choices=[('Flask','flask'), ('My-thoughts', 'my-thoughts'), ('Anglar','angular')], validators=[Required()])
    submit = SubmitField('Create Post')
    
class CommentForm(FlaskForm):
    comment = TextAreaField('Write your comment',validators=[Required()])
    submit = SubmitField("Submit Comment")