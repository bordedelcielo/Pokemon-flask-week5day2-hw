from flask_wtf import FlaskForm
from wtforms  import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class UserCreationForm(FlaskForm):
    user_input = StringField('user_input', validators=[DataRequired()])
    submit = SubmitField()

class Signup_Form(FlaskForm):
    first_name= StringField('first_name', validators=[DataRequired()])
    last_name= StringField('last_name', validators=[DataRequired()])
    email= StringField('email', validators=[DataRequired()])
    password= PasswordField('password', validators=[DataRequired()])
    confirm_password= PasswordField('confirm_password', validators=[DataRequired(), EqualTo('password')])
    submit= SubmitField()

class Login_Form(FlaskForm):
    email= StringField('email', validators=[DataRequired()])
    password= PasswordField('password', validators=[DataRequired()])
    confirm_password= PasswordField('confirm_password', validators=[DataRequired(), EqualTo('password')])
    submit= SubmitField()

class PokeForm(FlaskForm):
    pokemon = StringField('', validators= [DataRequired()])
    submit = SubmitField('Submit')

class EditProfile(FlaskForm):
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    email = StringField('email', validators = [DataRequired()])
    password = PasswordField('password', validators= [DataRequired()])
    confirm_password= PasswordField('confirm_password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField()
