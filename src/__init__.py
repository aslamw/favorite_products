from flask import Flask
from flask_cors import CORS
from flask_caching import Cache

from dotenv import load_dotenv
import os

from .Models import db, ma
from .Routes import api_client, api_favorite

load_dotenv()

app = Flask(__name__)

CORS(app)


#config database
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
local = os.getenv("MYSQL_HOST")
database = os.getenv("MYSQL_DATABASE")
port = os.getenv("MYSQL_PORT")



app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql+pymysql://{user}:{password}@{local}/{database}'

db.init_app(app)
ma.init_app(app)

#config cache
cache =Cache(app)
app.config['CACHE_TY PE'] = 'simple'
app.config['CACHE_DEFAULT_TIMEOUT'] = 60


from .Models import Client, Favorite_Product

#config route
app.register_blueprint(api_client)
app.register_blueprint(api_favorite)