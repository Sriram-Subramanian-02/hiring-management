from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.main.routes import main
    from app.resume_shortlisting.routes import resume_shortlisting
    
    app.register_blueprint(main)
    app.register_blueprint(resume_shortlisting)
    return app