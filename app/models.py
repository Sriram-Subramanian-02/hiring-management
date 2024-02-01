from app import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    type = db.Column(db.ChoiceType(["Applicant", "Company"]))
    address = db.Column(db.String(200))
    skills = db.Column(db.String(200))
    gender = db.Column(db.ChoiceType(["Male", "Female"]))
    state = db.Column(db.String(50))
    job_description = db.Column(db.Text)
    experience = db.Column(db.Integer)


# class Users(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))