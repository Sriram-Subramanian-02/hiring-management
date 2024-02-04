from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def user_loader(user_id):
    return db.session.query(Users).filter(Users.id == int(user_id)).first()


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    # type = db.Column(db.ChoiceType(["Applicant", "Company"]))
    address = db.Column(db.String(200))
    skills = db.Column(db.String(200))
    # gender = db.Column(db.ChoiceType(["Male", "Female"]))
    state = db.Column(db.String(50))
    job_description = db.Column(db.Text)
    experience = db.Column(db.Integer)
    password = db.Column(db.String(200))


# class Users(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     skills = db.Column(db.String(200))