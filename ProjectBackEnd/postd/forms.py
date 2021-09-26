from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,Length,Email
from wtforms.widgets import TextArea

class ContactFrom(FlaskForm):
    fulname=StringField('fulname',validators=[DataRequired(),Length(min=3,max=77)])
    email=StringField('email',validators=[DataRequired(),Email()])
    message=TextAreaField('message',validators=[DataRequired()],widget=TextArea())
    submit=SubmitField('Send')

