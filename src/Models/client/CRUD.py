from .table import Client, client_schema, db, clients_schema
    
    
    
def exist_or_get(key, value):
    """
    The function takes a key-value pair and returns a client object if it exists in the database,
    otherwise it returns None.
    
    :param key: The key parameter is a string that specifies the attribute of the Client object that we
    want to search for. It can be "email", "id", or "name"
    :param value: The value to search for in the database based on the key provided. For example, if the
    key is "email", the value parameter would be the email address to search for in the Client table
    """
    
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
    """
    The function creates a new client in the database and returns the client's information in JSON
    format.
    
    :param data: The `data` parameter is a dictionary that contains information about a client,
    including their name and email
    :return: a serialized representation of the newly created client object in the form of a JSON
    response.
    """
    
    client = Client(data["name"], data["email"])
    
    db.session.add_all([client])
    db.session.commit()
    
    response = client_schema.dump(client)
    
    return response



def update(data, client):
    """
    This function updates a client's name and email in the database and returns the updated client
    information.
    
    :param data: a dictionary containing the updated information for the client
    :param client: The `client` parameter is an instance of a `Client` model object. It represents a
    single client in a database
    :return: a serialized representation of the updated client object.
    """ 
    
    if data.get("name") is not None:
        client.name = data["name"]
        
    if data.get("email") is not None:
        client.email = data["email"]
    
    db.session.commit()
    
    response = client_schema.dump(client)
    
    return response


    
def delete(client):
    """
    This function deletes a client from the database.
    
    :param client: The parameter `client` is likely an instance of a client model object in a Flask
    application. The `delete` function is likely used to delete this client object from the database by
    calling `db.session.delete(client)` and then committing the changes to the database with
    `db.session.commit()`
    """

    db.session.delete(client)
    db.session.commit()
    
    
    
def All():
    """
    The function retrieves all clients from the database and returns them as a serialized response.
    :return: a response object that contains a serialized list of all clients in the database. The
    serialization is done using the clients_schema object, which is a schema object that defines how the
    Client model should be serialized.
    """
    
    clients = Client.query.all()
    
    response = clients_schema.dump(clients)
    
    return response