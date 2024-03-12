from app import db, login_manager
from flask_login import UserMixin
from sqlalchemy_utils import ChoiceType


@login_manager.user_loader
def user_loader(user_id):
    return db.session.query(Users).filter(Users.id == int(user_id)).first()


class Users(db.Model, UserMixin):
    TYPES = [
        ('admin', 'Admin'),
        ('candidate', 'Candidate'),
        ('hr', 'HR')
    ]

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    type = db.Column(db.String(50))
    phone_no = db.Column(db.Integer)
    skills = db.Column(db.String(200))
    gender = db.Column(db.String(50))
    state = db.Column(db.String(50))
    job_description = db.Column(db.Text)
    experience = db.Column(db.Integer)
    password = db.Column(db.String(200))


class VectorDBId(db.Model):
    id = db.Column(db.Integer, primary_key=True)