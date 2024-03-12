import os
from dotenv import load_dotenv

from flask import render_template, url_for, flash, redirect, Blueprint, request
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.utils import secure_filename
from app.users.forms import RegistrationForm, LoginForm, UploadFileForm, FillJobDescription
from app import db, bcrypt
from app.users.models import Users
from app.users.services import store_resume, search_candidates_vector_db

load_dotenv(dotenv_path= os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

users = Blueprint('users', __name__)


@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Users(
                name = form.name.data, 
                email = form.email.data, 
                password = hashed_password, 
                phone_no = form.phone.data,
                type = form.type.data,
                gender = form.gender.data,
                experience = form.experience.data
            )
        db.session.add(user)
        db.session.commit()

        flash(f'Account created for {form.name.data}!', 'success')
        return redirect(url_for('users.login'))
    
    return render_template('register.html', title='Register', form=form)


@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("main.home"))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    
    return render_template('login.html', title='Login', form=form)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("users.login"))


@users.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')


@users.route("/file_upload", methods=['GET', 'POST'])
@login_required
def file_upload():
    form = UploadFileForm()
    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        form.file.data.save(os.getenv("RESUME_FILE_PATH") + filename)
        insert_resume = store_resume(current_user.name, current_user.email, current_user.phone_no, os.getenv("RESUME_FILE_PATH") + filename)
        insert_resume.insert_resume()
        
        # return redirect(url_for('users.file_upload'))
        return "Successfully Inserted Resume Data into Vector DB"
    return render_template('file_upload.html', title='Upload Resume', form=form)


@users.route("/search_candidates", methods=['GET', 'POST'])
@login_required
def search_candidates():
    form = FillJobDescription()
    if form.validate_on_submit():
        print(form.job_description.data)
        # return form.job_description.data
        # search_data = search_candidates(form.job_description.data)
        search_data = search_candidates_vector_db(form.job_description.data)
        return search_data.search()
    return render_template('job_description.html', title='Search Candidates', form=form)