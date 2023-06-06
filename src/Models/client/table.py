from .. import db, ma
import datetime

class Client(db.Model):
    __tablename__ = 'client'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    
    date_create = db.Column(db.DateTime, default=datetime.datetime.now())
    
    favorite = db.relationship("Favorite_Product", cascade="all, delete", backref="client")
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    
    
class ClientSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "email", 'date_create')
        
client_schema = ClientSchema()
clients_schema = ClientSchema(many=True)