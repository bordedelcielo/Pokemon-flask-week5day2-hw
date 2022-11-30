from flask_wtf import FlaskForm
from wtforms  import StringField, SubmitField
from wtforms.validators import DataRequired

class UserCreationForm(FlaskForm):
    user_input = StringField('user_input', validators=[DataRequired()])
    submit = SubmitField()