from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_caching import Cache
from dotenv import load_dotenv
import os

from .Models import db, ma
from .Routes import api_client

load_dotenv()

app = Flask(__name__)

CORS(app)

#config cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
CASH_TIMEOUT = 60

#config database
bank = os.getenv("BANK")
database = os.getenv("DATABASE")

app.config["SQLALCHEMY_DATABASE_URI"] = f"{bank}:///{database}"
app.config["SQLALCHEMY_BINDS"] = {
    "in_memory": "sqlite:///:memory:"
}

db.init_app(app)
ma.init_app(app)

mi = Migrate(app, db)

from .Models import Client, Favorite_Product

app.register_blueprint(api_client)