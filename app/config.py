import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')