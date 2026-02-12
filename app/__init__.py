from flask import Flask,session
from config import BaseConfig
from flask_sqlalchemy import SQLAlchemy

#import reusableLibraries

app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)


print(app.config["SECRET_KEY"])
print(app.config["SQLALCHEMY_DATABASE_URI"])

# All the commented line deleted

#git commit

from app import routes

