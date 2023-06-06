from flask import Blueprint, request, jsonify
from ..Controllers import create_client, update_client, delete_client, get_email, get_id, get_name

import json



api_client = Blueprint('client', __name__)

@api_client.get('/')
def base():
    return jsonify({"mensage":"ok"}),200

@api_client.post("/client/create/")
def route_create_client():
    data = json.loads(request.data) 
    
    return create_client(data)

@api_client.put("/client/update/<int:client_id>/")
def route_update_client(client_id:int):
    
    data:dict = json.loads(request.data) 
    
    return update_client(client_id, data)

@api_client.get("/client/<int:client_id>/")
def get_client(client_id):
    
    return get_id(client_id)


@api_client.get("/client/")
def get_client_by_query():
    email = request.args.get('email')
    name = request.args.get('name')
    
    print(email)
    if email is not None:
        client = get_email(email)
        
    elif name is not None:
        client = get_name(name)
        
    else: return jsonify({"menssage": "No parameters provided"}),400
    
    return client
    



@api_client.delete("/client/delete/<int:client_id>/")
def update_delete_client(client_id):
    
    return delete_client(client_id)
