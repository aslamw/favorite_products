from .table import Favorite_Product, favorite_schema, db
import datetime
    
def exist_or_get(key, value):
    
    match key:
        
        case "email":
            client = Favorite_Product.query.filter(Favorite_Product.email == value).first()
            
        case  "id":
            client = Favorite_Product.query.filter(Favorite_Product.id == value).first()
        
        case "name":
            client = Favorite_Product.query.filter(Favorite_Product.name == value).first()
            
        case _:
            return None
        
    db.session.commit()
    
    if client is not None:
        return client
    
    
    return None
    

def create(data):
    
    client = Favorite_Product(data["name"], data["email"])
    
    db.session.add_all([client])
    db.session.commit()
    
    response = client_schema.dump(client)
    
    return response

def update(id, data):
    
    client = Favorite_Product.query.get(id)  
    
    if data.get("name") is not None:
        client.name = data["name"]
        
    if data.get("email") is not None:
        client.email = data["email"]
    
    db.session.commit()
    
    response = client_schema.dump(client)
    
    return response

def delete(id):
    
    client = Client.query.get(id)  
    
    client.state_client = False
    
    client.date_delete = datetime.datetime.now()
    
    db.session.commit()
    
    response = client_schema.dump(client)
    
    return response
    
def force_delete(id):
    
    client = Client.query.get(id)
    
    db.session,delete(client)
    db.session.commit()
    
    return client