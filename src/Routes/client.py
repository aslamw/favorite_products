from flask import Blueprint, request, jsonify
from ..Controllers import create_client, update_client, delete_client, get_email, get_id, get_name, get_all_client
from ..Controllers import auth
import json


api_client = Blueprint('client', __name__)



@api_client.get('/')
def base():
    """
    This function returns a JSON response with a message "ok" and a status code of 200 when the root
    endpoint is accessed.
    :return: A JSON response with the message "ok" and a status code of 200.
    """
    return jsonify({"mensage":"ok"}),200



@api_client.post("/client/create/")
@auth
def route_create_client():
    """
    This function creates a new client using data from a JSON request and requires authentication.
    :return: The function `route_create_client()` is returning the result of the function
    `create_client(data)`. The specific return value of `create_client(data)` depends on the
    implementation of that function.
    """
    data = json.loads(request.data) 
    
    return create_client(data)



   
@api_client.put("/client/update/<int:client_id>/")
@auth
def route_update_client(client_id:int):
    """
    This is a Python function that updates a client's data using a PUT request and authentication.
    
    :param client_id: The client ID is an integer value that is passed as a parameter to the
    route_update_client function. It is used to identify the specific client that needs to be updated in
    the database
    :type client_id: int
    :return: The function `route_update_client` is returning the result of calling the `update_client`
    function with the `client_id` and `data` as arguments.
    """
    
    data:dict = json.loads(request.data) 
    
    return update_client(client_id, data)



    
@api_client.get("/client/<int:client_id>/")
@auth
def get_client(client_id):
    """
    This function retrieves a client's information by their ID and requires authentication.
    
    :param client_id: The client_id parameter is an integer that represents the unique identifier of a
    client. It is used to retrieve information about a specific client from the API
    :return: The function `get_client` is returning the result of calling the function `get_id` with the
    argument `client_id`. The specific result that is returned depends on the implementation of the
    `get_id` function.
    """
    
    return get_id(client_id)


    
@api_client.get("/client/")
@auth
def get_client_by_query():
    """
    This function retrieves a client by either their email or name through a GET request with
    authentication.
    :return: This code defines a function that receives a GET request to the endpoint "/client/" with
    optional query parameters "email" and "name". The function first checks if the "email" parameter is
    provided and calls the function "get_email" to retrieve the client with that email. If not, it
    checks if the "name" parameter is provided and calls the function "get_name" to retrieve the client
    """
    
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
@auth
def update_delete_client(client_id):
    """
    This function is a decorator that deletes a client with a specific ID after authenticating the user.
    
    :param client_id: The client ID is an integer value that identifies a specific client in the system.
    It is used as a parameter in the URL path to specify which client should be deleted
    :return: The function `update_delete_client` is returning the result of calling the `delete_client`
    function with the `client_id` parameter. The `delete_client` function is not shown in the code
    snippet provided, so it is unclear what it returns.
    """
    return delete_client(client_id)



    
@api_client.get("/client/all")
@auth
def get_all():
    """
    This function uses an API client to get all clients and requires authentication.
    :return: The function `get_all()` is returning the result of calling the function
    `get_all_client()`. The specific content of the returned value depends on the implementation of
    `get_all_client()`.
    """
    return get_all_client()
