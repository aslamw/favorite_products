from flask import Blueprint, request, jsonify
from ..Controllers import create_favorite_product, add_favorite_product, remove_favorite_product, get_product, get_all_product
from ..Controllers import auth
import json

api_favorite = Blueprint('product', __name__)



@api_favorite.post('/product/<int:client_id>/')
@auth
def route_create_favorite(client_id):
    """
    This function creates a favorite product for a specific client using their client ID and the product
    ID provided in the request data.
    
    :param client_id: The ID of the client who is creating the favorite product
    :return: The function `route_create_favorite` is returning the result of calling the function
    `create_favorite_product` with the `client_id` and `product_id` extracted from the request data. The
    specific value being returned depends on the implementation of `create_favorite_product`.
    """
    data = json.loads(request.data)
    
    return create_favorite_product(client_id, data['product_id'])



    
@api_favorite.put('/product/add/<int:client_id>/')
@auth
def route_add_favorite(client_id):
    """
    This function adds a product to a client's list of favorite products.
    
    :param client_id: The client ID is an integer value that identifies a specific client in the system.
    It is used as a parameter in the URL path to specify which client's favorite products are being
    modified
    :return: The function `route_add_favorite` is returning the result of calling the
    `add_favorite_product` function with the `client_id` and `product_id` extracted from the request
    data. The specific return value of `add_favorite_product` is not shown in this code snippet.
    """
    data = json.loads(request.data)
    
    return add_favorite_product(client_id, data['product_id'])




    
@api_favorite.delete('/product/remove/<int:client_id>/')
@auth
def route_remove_favorite(client_id):
    """
    This function removes a favorite product for a specific client using their client ID and the product
    ID.
    
    :param client_id: The client ID is an integer value that identifies a specific client who has added
    a product to their favorites list. This ID is used to retrieve the client's favorites list and
    remove a specific product from it
    :return: The function `route_remove_favorite` is returning the result of calling the
    `remove_favorite_product` function with the `client_id` and `product_id` extracted from the request
    data. The specific data type of the returned value is not specified in the code snippet provided.
    """
    data = json.loads(request.data)
    
    return remove_favorite_product(client_id, data['product_id'])




    
@api_favorite.get('/product/<int:client_id>/')
@auth
def route_get_product(client_id):
    """
    This is a Flask route that returns a product for a given client ID, and requires authentication.
    
    :param client_id: client_id is an integer parameter that is used to identify a specific client in
    the system. It is passed as a parameter in the URL path of the API endpoint. The function
    `route_get_product` uses this parameter to call the `get_product` function and retrieve information
    about the product associated with the
    :return: The function `route_get_product` is returning the result of calling the function
    `get_product` with the `client_id` parameter passed to it. The specific data or object being
    returned by `get_product` is not specified in the code snippet provided.
    """
    
    return get_product(client_id)



    
@api_favorite.get('/product/all')
@auth
def route_get_all():
    """
    This function returns all products and requires authentication.
    :return: The function `get_all_product()` is being called and its return value is being returned as
    the response to the GET request to the endpoint `/product/all`. The specific content of the response
    depends on the implementation of `get_all_product()`.
    """
    
    return get_all_product()