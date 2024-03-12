from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///postgres.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:sriram@localhost/sg"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    # app.config['UPLOAD_FOLDER'] = 'F:\\psg\\sem_8\\hiring-management\\app\\resumes'

    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    

    from app.main.routes import main
    from app.resume_shortlisting.routes import resume_shortlisting
    from app.users.routes import users
    
    app.register_blueprint(main)
    app.register_blueprint(resume_shortlisting)
    app.register_blueprint(users)
    return app