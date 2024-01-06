from flask import Flask
from app.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.main.routes import main
    from app.resume_shortlisting.routes import resume_shortlisting
    from app.users.routes import users
    
    app.register_blueprint(main)
    app.register_blueprint(resume_shortlisting)
    app.register_blueprint(users)
    return app