from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo
from wtforms.widgets import TextArea
from flask_ckeditor import CKEditorField


class SignUpForm(FlaskForm):
    """Defines Validators for  user sign-up form"""
    username = StringField(label='Username', validators=
                           [InputRequired(message="User name should not be blank"),
                            Length(min=5,max=25)])

    email = StringField(label='Email Address',
                        validators=[InputRequired(message="email name should not be blank"),
                                    Length(max=45, message="Email should have less than 45 characters")])

    password = PasswordField(label='Password', validators=
                             [InputRequired(message="Password should not be left blank"),
                              Length(max=10, message="Password too long")])

    confirm_password = PasswordField(label='Confirm Password', validators=
                             [InputRequired(message="Password should not be left blank"),
                              Length(max=10, message="Password too long"),
                              EqualTo('password', message="Passwords do not match")])

    submit = SubmitField(label= 'Sign Up')


class LoginForm(FlaskForm):
    """Defines validators for user login form"""
    password = PasswordField(label='Password',
                             validators=[InputRequired(message='Password cannot be blank'),
                                         Length(max=10, message=('Password should be less than 10 characters'))])
    
    submit = SubmitField(label= 'Sign Up')

    email = StringField(label='Email Address', validators=
                           [InputRequired(message="email name should not be blank"),
                            Length(max=45, message="Email should have less than 45 characters")])


class ContactForm(FlaskForm):
    """Stores user input in database"""
    email = StringField(label='Email Address',
                        validators=[InputRequired(message="email name should not be blank"),
                                    Length(max=45, message="Email should have less than 45 characters")])

    full_name = StringField(label='Full Name', validators=[InputRequired(message='Tells us who you are.'),
                                                           Length(max=50, message="Name should be less than 50 characters")])
    
    message = TextAreaField(label='Enter your message')

class PostForm(FlaskForm):
    """Form for blog creattion"""
    title = StringField(label='Title',
                        validators=[InputRequired(message="Title cannot be left blank")])

    summary = StringField(label='Description', validators=[InputRequired(message='This field cannot be blank'),
                                                     Length(max=200, message='Description must be less then 200 characters')])
    
    content = CKEditorField('AI Content', validators=[InputRequired(message='This field cannot be blank')])

    submit = SubmitField(label= 'Save')


