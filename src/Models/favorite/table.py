from .. import db, ma, Client


class Favorite_Product(db.Model):
    __tablename__ = 'favorite_product'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, db.ForeignKey("client.id"), nullable=False)
    favorite_product= db.Column(db.JSON)
    
class Favorite_Product_Schema(ma.Schema):
    class Meta:
        fields = ("id", "client_id", "favorite_product")
        
favorite_schema = Favorite_Product_Schema()
favorites_schema = Favorite_Product_Schema(many=True)
    