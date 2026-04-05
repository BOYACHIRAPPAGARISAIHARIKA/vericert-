# Flask Configuration

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Paths for Models
    USER_MODEL_PATH = 'app.models.user'
    POST_MODEL_PATH = 'app.models.post'