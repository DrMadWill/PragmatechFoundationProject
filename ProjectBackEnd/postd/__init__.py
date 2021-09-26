from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import os
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/img/')



app=Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resault.db'
app.config['SECRET_KEY']='mimlmimg7'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



from postd import routes