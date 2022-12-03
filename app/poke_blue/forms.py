from flask_wtf import FlaskForm
from wtforms  import StringField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title= StringField('Title', validators=[DataRequired()])
    img_url= StringField('Image_URL', validators=[DataRequired()])
    caption= StringField('Caption', validators=[DataRequired()])
    submit_btn= SubmitField()