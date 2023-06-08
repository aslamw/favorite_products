from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
ma = Marshmallow()

from .client.table import Client,client_schema
from .client.CRUD import exist_or_get, create, delete, update, All

from .favorite.table import Favorite_Product, favorite_schema
from .favorite.CRUD import exist_or_get_favorite, create_favorite, update_favorite, delete_favorite, All_product