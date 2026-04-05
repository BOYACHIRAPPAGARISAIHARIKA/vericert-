from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database configuration
DB_USER = 'your_user'
DB_PASSWORD = 'your_password'
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'your_database'

# SQLAlchemy setup
DATABASE_URL = f'mysql+pymysql://{{DB_USER}}:{{DB_PASSWORD}}@{{DB_HOST}}:{{DB_PORT}}/{{DB_NAME}}'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)