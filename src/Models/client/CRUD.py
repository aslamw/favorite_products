from .table import Client, client_schema, db
import datetime
    
def exist_or_get(key, value):
    
    match key:
        
        case "email":
            client = Client.query.filter(Client.email == value).first()
            
        case  "id":
            client = Client.query.filter(Client.id == value).first()
        
        case "name":
            client = Client.query.filter(Client.name == value).first()
            
        case _:
            return None
    
    if client is not None:
        return client
    
    
    return None
    

def create(data):
    
    client = Client(data["name"], data["email"])
    
    db.session.add_all([client])
    db.session.commit()
    
    response = client_schema.dump(client)
    
    return response

def update(data, client):
    
    #client = Client.query.get(id)  
    
    if data.get("name") is not None:
        client.name = data["name"]
        
    if data.get("email") is not None:
        client.email = data["email"]
    
    db.session.commit()
    
    response = client_schema.dump(client)
    
    return response

    
def delete(client):

    db.session.delete(client)
    db.session.commit()