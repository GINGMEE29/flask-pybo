import os

BASE_DIR = os.path.dirname(__file__)
SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://admin:finman12@localhost:3306/samples?charset=utf8"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"