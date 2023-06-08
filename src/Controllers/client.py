from ..Models import create, update, exist_or_get, delete, client_schema, All
from flask import jsonify

import re

#fomat valid email
F_email = re.compile(r'^[\w-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$')



    
def create_client(data):
    """
    This function creates a client with given data and returns an error message if any of the mandatory
    fields are missing or invalid.
    
    :param data: The input data for creating a new client, which should include the client's name and
    email address
    :return: The function `create_client` returns a JSON response with a message and a status code. The
    message and status code depend on the conditions met in the function. If all fields are mandatory,
    it returns a message "All fields are mandatory" and a status code 400. If the name is invalid, it
    returns a message "name invalid" and a status code 400. If the email is
    """
    try:
    
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
    
    except:
        return jsonify({"message":"internal error"}),500



def update_client(id, data):
    """
    This function updates a client's information in a database, checking for errors such as invalid name
    or email and existing email.
    
    :param id: The ID of the client to be updated
    :param data: The data parameter is a dictionary containing the updated information for the client.
    It can contain the keys 'name' and 'email', which correspond to the client's name and email address,
    respectively
    :return: a JSON response with a message and a status code. The message and status code depend on the
    outcome of the function's execution. If the function executes successfully, it returns a JSON
    response with the updated data and a status code of 200. If there is an error, it returns a JSON
    response with an error message and a status code of 400 or 500, depending on
    """
    try:
    
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
    
    except:
        return jsonify({"message":"internal error"}),500



def get_id(id):
    """
    This function retrieves a client's information by their ID and returns a JSON response with the
    information or an error message.
    
    :param id: The parameter "id" is a variable that represents the unique identifier of a client. It is
    used in the function "get_id" to retrieve information about a client from a database
    :return: The function `get_id` returns a JSON response with a message indicating whether the
    requested `id` exists in the system or not, along with an HTTP status code. If the `id` exists, the
    function also returns the client information associated with that `id`. If there is an internal
    error, the function returns a JSON response with a message indicating the error and an HTTP status
    code of
    """
    try:
    
        if (client := exist_or_get('id',id)) is None:
            return jsonify({'menssage':'this id not exists'}),400
        
        return jsonify(client_schema.dump(client)),200
    
    except:
        return jsonify({"message":"internal error"}),500



def get_name(name):
    """
    This function takes a name as input, checks if it exists in a database, and returns either the
    client information or an error message.
    
    :param name: The parameter "name" is a string that represents the name of a client. It is used as
    input to the function "exist_or_get" to check if the client exists in the system and retrieve its
    information if it does. If the client does not exist, the function returns a JSON response with
    :return: The function `get_name` returns a JSON response with either the client information and a
    status code of 200 if the client exists, or a message indicating that the name does not exist and a
    status code of 400. If there is an internal error, it returns a message with a status code of 500.
    """
    try:
    
        if (client := exist_or_get('name',name)) is None:
            return jsonify({'menssage':'this name not exists'}),400
        
        return jsonify(client_schema.dump(client)),200
    
    except:
        return jsonify({"message":"internal error"}),500



def get_email(email):
    """
    This function takes an email as input, checks if it exists in a database, and returns either the
    client information or an error message.
    
    :param email: The email parameter is a string that represents the email address of a client. This
    function is designed to retrieve information about a client based on their email address
    :return: The function `get_email` returns a JSON response with either the client information and a
    status code of 200 if the email exists in the database, or a message indicating that the email does
    not exist and a status code of 400. If there is an internal error, it returns a message with a
    status code of 500.
    """
    try:
    
        if (client := exist_or_get('email',email)) is None:
            return jsonify({'menssage':'this email not exists'}),400
        
        return jsonify(client_schema.dump(client)),200
    
    except:
        return jsonify({"message":"internal error"}),500



def delete_client(id):
    """
    This function deletes a client with a given ID and returns a success message, an error message if
    the ID does not exist, or an internal error message.
    
    :param id: The parameter `id` is the unique identifier of the client that needs to be deleted from
    the system
    :return: a JSON response with a message and a status code. If the client with the given ID exists
    and is successfully deleted, the message "Client deleted" and a status code of 200 are returned. If
    the client with the given ID does not exist, the message "This ID does not exist" and a status code
    of 400 are returned. If there is an internal error
    """
    try:
    
        if (client := exist_or_get('id', id)) is not None:
            
            delete(client)
            return jsonify({'message': 'Client deleted'}), 200
        else:
            return jsonify({'message': 'This ID does not exist'}), 400
        
    except:
        return jsonify({"message":"internal error"}),500
    
    
    
    
def get_all_client():
    """
    This function retrieves all clients and returns them as a JSON object with a status code of 200, or
    returns a JSON error message with a status code of 500 if there is an internal error.
    :return: a JSON response with a list of all clients and a status code of 200 if there are no errors.
    If there is an error, it returns a JSON response with an error message and a status code of 500.
    """
    
    try:
        clients = All()
    
        return jsonify(clients),200
    
    except:
        return jsonify({"message":"internal error"}),500
