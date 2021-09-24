
from postd import db

from flask_sqlalchemy import SQLAlchemy

# -------------------Main Website----------------------


# -------------------Home Iformation----------------------
class Homein(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.String(80), nullable=False)
    infoimg=db.Column(db.String(100))
    

    def __repr__(self):
        return '<Homein %r>' % self.info

# -------------------About Iformation----------------------

class Aboutin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aboutinfo1 = db.Column(db.String(160), nullable=False)
    aboutinfo2 = db.Column(db.String(160), nullable=False)
    disgen1 = db.Column(db.String(25),nullable=False)
    disgen1interest = db.Column(db.Integer,nullable=False)
    disgen2 = db.Column(db.String(25),nullable=False)
    disgen2interest = db.Column(db.Integer,nullable=False)
    disgen3 = db.Column(db.String(25),nullable=False)
    disgen3interest = db.Column(db.Integer,nullable=False)
    disgen4 = db.Column(db.String(25),nullable=False)
    disgen4interest = db.Column(db.Integer,nullable=False)
    disgen5 = db.Column(db.String(25),nullable=False)
    disgen5interest = db.Column(db.Integer,nullable=False)
    aboutinfoimg=db.Column(db.String(100))
    

    def __repr__(self):
        return '<Aboutin %r>' % self.aboutinfo1

# -------------------MyProject Iformation----------------------
class Projectin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    protime = db.Column(db.String(25), nullable=False)
    protitle = db.Column(db.String(50), nullable=False)
    prosortcut = db.Column(db.String(80), nullable=False)
    proimg=db.Column(db.String(100))
    

    def __repr__(self):
        return '<Projectin %r>' % self.protitle




class Contactin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fulname = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(200), nullable=False)
    
    

    def __repr__(self):
        return '<Contactin %r>' % self.protitle
