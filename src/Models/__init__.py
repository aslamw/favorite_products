from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from .client.table import Client
from .client.CRUD import exist, get_by_id, create


db = SQLAlchemy()
ma = Marshmallow()