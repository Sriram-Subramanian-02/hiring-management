from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, BooleanField, SelectMultipleField, ValidationError, FileField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired
from app.users.models import Users


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[DataRequired()])

    # Dropdown for Gender
    gender_choices = [('Male', 'Male'), ('Female', 'Female')]
    gender = SelectField('Gender', choices=gender_choices)

    # Dropdown for Type
    type_choices = [('Applicant', 'Applicant/Candidate'), ('Company', 'Company')]
    type = SelectField('Type', choices=type_choices, validators=[DataRequired()])

    # Multiple values for Skills
    skills_choices = [('Python', 'Python'), ('JavaScript', 'JavaScript'), ('SQL', 'SQL'), ('Other', 'Other')]
    skills = SelectMultipleField('Skills', choices=skills_choices, validators=[DataRequired()])

    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    # Integer only for Experience
    experience = StringField('Experience', validators=[DataRequired()])

    submit = SubmitField('Sign Up')


    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")


class FillJobDescription(FlaskForm):
    job_description = StringField('Job Description', validators=[DataRequired(), Length(min=1, max=500)])
    submit = SubmitField('Search')