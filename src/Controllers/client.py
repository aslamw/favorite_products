from ..Models import create, update, exist_or_get, delete, client_schema
from flask import jsonify

import re

#fomat valid email
F_email = re.compile(r'^[\w-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$')

def create_client(data):
    
    if data.get('name') is None or data.get('email') is None:
        return jsonify({"menssage":"All fields are mandatory"}),400
    
    if not re.search(r'^[A-Za-z\s]+$', data['name']):
        return jsonify({"menssage":"name invalid"}),400
    
    if not F_email.match(data['email']):
        return jsonify({'menssage':"invalid email"}),400
    
    if exist_or_get('email',data['email']) is not None:
        return jsonify({'menssage':'this email already exists'}),400
    
    client = create(data)
    
    return jsonify(client),201


def update_client(id, data):
    
    if (client := exist_or_get('id',id)) is None:
        return jsonify({'menssage':'this id not exists'}),400
    
    if data.get('name') is not None:
    
        if not re.search(r'^[A-Za-z\s]+$', data['name']):
            return jsonify({"menssage":"name invalid"}),400
        
    if data.get('email') is not None:
    
        if not F_email.match(data['email']):
            return jsonify({'menssage':"invalid email"}),400
    
        if exist_or_get('email',data['email']) is not None:
            return jsonify({'menssage':'this email already exists'}),400
    
    response = update(data, client)
    
    return jsonify(response),200

def get_id(id):
    
    if (client := exist_or_get('id',id)) is None:
        return jsonify({'menssage':'this id not exists'}),400
    
    return jsonify(client_schema.dump(client)),200

def get_name(name):
    
    if (client := exist_or_get('name',name)) is None:
        return jsonify({'menssage':'this name not exists'}),400
    
    return jsonify(client_schema.dump(client)),200

def get_email(email):
    
    if (client := exist_or_get('email',email)) is None:
        return jsonify({'menssage':'this email not exists'}),400
    
    return jsonify(client_schema.dump(client)),200

def delete_client(id):
    
    if (client := exist_or_get('id', id)) is not None:
        
        delete(client)
        return jsonify({'message': 'Client deleted'}), 200
    else:
        return jsonify({'message': 'This ID does not exist'}), 400
