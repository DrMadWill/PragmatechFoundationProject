from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
from werkzeug.utils import secure_filename
import os
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/img/')



app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resault.db'
db = SQLAlchemy(app)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class Homein(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.String(80), nullable=False)
    infoimg=db.Column(db.String(200))
    

    def __repr__(self):
        return '<User %r>' % self.info


class Aboutin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aboutinfo1 = db.Column(db.String(160), nullable=False)
    aboutinfo2 = db.Column(db.String(160), nullable=False)
    disgen1 = db.Column(db.String(25))
    disgen1interest = db.Column(db.String(5))
    aboutinfoimg=db.Column(db.String(200))
    

    def __repr__(self):
        return '<User %r>' % self.aboutinfo1


class Projectin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    protime = db.Column(db.String(25), nullable=False)
    protitle = db.Column(db.String(50), nullable=False)
    prosortcut = db.Column(db.String(80), nullable=False)
    aboutinfoimg=db.Column(db.String(200))
    

    def __repr__(self):
        return '<User %r>' % self.protitle

# HomeInf=['We make beautiful websites for all people.']



# infose =[
#     {
#         'cardTime':'December 25.07.21`',
#         'cardTitle':'how to become a web developer',
#         'cardText':'Lorem ipsum dolor sit consectetur adipiscing morbi venenatis.'
#     },
#     {
#         'cardTime':'December 25.07.21`',
#         'cardTitle':'how to become a web developer',
#         'cardText':'Lorem ipsum dolor sit consectetur adipiscing morbi venenatis.'
#     }

# ]

