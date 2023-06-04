from .table import Client, client_schema, db

def exist(data):
    
    client = Client.query.filter(Client.name == data['email']).one()
    
    if not client:
        return False
    
    return True
    

def create(data):
    
    client = Client(data["name"], data["email"])
    
    db.session.add_all([client])
    db.session.commit()
    
    response = client_schema.dump(client)
    
    return response