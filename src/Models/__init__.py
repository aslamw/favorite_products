from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
ma = Marshmallow()

from .client.table import Client,client_schema
from .client.CRUD import exist_or_get, create, delete, update

from .favorite.table import Favorite_Product
#from .favorite.CRUD import *