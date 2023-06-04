from flask import Flask
from flask_cors import CORS
from flask_migrate import migrate
from dotenv import load_dotenv
import os

from Models import db, ma

load_dotenv()

app = Flask(__name__)
CORS(app)

bank = os.getenv("BANK")
database = os.getenv("DATABASE")

app.config["SQLALCHEMY_DATABASE_URI"] = f"{bank}:///{database}"

db.init_app(app)
ma.init_app(app)

mi = migrate(app, db)

from Models import Client