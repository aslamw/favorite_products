from .. import db, ma


class Client(db.Model):
    __table__ = 'client'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    favorite_products = str
    
class ClientSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "email")
        
client_schema = ClientSchema()
clients_schema = ClientSchema(many=True)