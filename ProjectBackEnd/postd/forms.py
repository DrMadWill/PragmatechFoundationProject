from flask_wtf import FlaskForm
from wtforms import StringField,TextField,SubmitField
from wtforms.validators import DataRequired,Length,Email


class Contactin(FlaskForm):
    full_name=StringField('')

