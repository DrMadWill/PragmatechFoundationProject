from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resault.db'
db = SQLAlchemy(app)



class homein(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.String(80), nullable=False)
    

    def __repr__(self):
        return '<User %r>' % self.info



# HomeInf=['We make beautiful websites for all people.']


infose =[
    {
        'cardTime':'December 25.07.21`',
        'cardTitle':'how to become a web developer',
        'cardText':'Lorem ipsum dolor sit consectetur adipiscing morbi venenatis.'
    },
    {
        'cardTime':'December 25.07.21`',
        'cardTitle':'how to become a web developer',
        'cardText':'Lorem ipsum dolor sit consectetur adipiscing morbi venenatis.'
    }

]

