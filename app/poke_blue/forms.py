from flask_wtf import FlaskForm
from wtforms  import StringField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    pokemon = StringField('', validators= [DataRequired()])
    submit = SubmitField('Submit')