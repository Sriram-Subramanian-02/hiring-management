from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///postgres.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:sriram@localhost/sg"

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

    db.init_app(app)
    migrate.init_app(app, db)

    from app.main.routes import main
    from app.resume_shortlisting.routes import resume_shortlisting
    from app.users.routes import users
    
    app.register_blueprint(main)
    app.register_blueprint(resume_shortlisting)
    app.register_blueprint(users)
    return app