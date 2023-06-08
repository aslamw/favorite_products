from ..Models import db, exist_or_get, exist_or_get_favorite, create_favorite, update_favorite, delete_favorite, All_product
from ..Api import get_product_id, validation_id
from flask import jsonify



def create_favorite_product(id_client, product_id):
    """
    This function creates a favorite product for a given client and product ID, with error handling for
    invalid IDs and existing favorites.
    
    :param id_client: The ID of the client for whom the favorite product is being created
    :param product_id: The ID of the product that the client wants to add to their favorites
    :return: a JSON response with a message indicating the result of the operation. If the operation is
    successful, it returns a message "favorite create" with a status code of 201. If there is an error,
    it returns a message indicating the type of error with a status code of 400 or 500.
    """
    
    try:
        if not validation_id(product_id):
            return jsonify({'menssage':'this product_id invalid'}),400
        
        client = exist_or_get('id', id_client)
        
        product = exist_or_get_favorite(id_client)
        
        if client is None:
            return jsonify({'menssage':'this client not exist'}),400
        
        if product is not None:
            return jsonify({'menssage':'this product exist'}),400
        
        product = create_favorite(id_client, product_id)
        
        client.favorite = product
        
        db.session.commit()
        
        return jsonify({'menssage':'favorite create'}),201
    
    except:
        return jsonify({"message":"internal error"}),500



def add_favorite_product(id_client, product_id):
    """
    This function adds a product to a client's favorite list and returns a message indicating success or
    failure.
    
    :param id_client: The ID of the client who wants to add a favorite product
    :param product_id: The product ID is a unique identifier assigned to a specific product in a system
    or database. It is used to distinguish one product from another and is often used in various
    operations such as adding, updating, or deleting products. In this case, the function is designed to
    add a product to a client's
    :return: a JSON response with a message indicating whether the favorite product was successfully
    added or not. If there is an error, it returns a JSON response with an error message and an
    appropriate status code.
    """
    
    try:
        if not validation_id(product_id):
            return jsonify({'menssage':'this product_id invalid'}),400
        
        base = exist_or_get_favorite(id_client)
        
        if base is None:
            return jsonify({'menssage':'this product not exist'}),400
        
        product = update_favorite(base, product_id)
        
        if not product:
            return jsonify({'menssage':"it's already in the favorite"}),400
        
        return jsonify({'menssage':'favorite add'}),200
    
    except:
        return jsonify({"message":"internal error"}),500



def remove_favorite_product(id_client, product_id):
    """
    This function removes a product from a client's list of favorite products and returns an appropriate
    message based on the success or failure of the operation.
    
    :param id_client: The ID of the client whose favorite product is being removed
    :param product_id: The ID of the product that the client wants to remove from their favorites
    :return: a JSON response with a message indicating whether the removal of the favorite product was
    successful or not. If there is an error, it returns a JSON response with an error message and a
    status code of 500.
    """
    
    try:
    
        if not validation_id(product_id):
            return jsonify({'menssage':'this product_id invalid'}),400
        
        base = exist_or_get_favorite(id_client)
        
        if base is None:
            return jsonify({'menssage':'this product not exist'}),400
        
        product = delete_favorite(base, product_id)
        
        if not product:
            return jsonify({'menssage':'does not exist in favorite'}),400
        
        return jsonify({'menssage':'favorite remove'}),200
    
    except:
        return jsonify({"message":"internal error"}),500



def get_product(id_client):
    """
    This function retrieves a list of favorite products for a given client ID and returns the product
    information in JSON format.
    
    :param id_client: The parameter `id_client` is an identifier for a client, which is used to retrieve
    their favorite products
    :return: a JSON response with either a list of favorite products for a given client ID or an error
    message if there is an internal error or if the product does not exist.
    """
    
    try:
    
        base = exist_or_get_favorite(id_client)
        
        if base is None:
            return jsonify({'menssage':'this product not exist'}),400
        
        product = exist_or_get_favorite(id_client)
        
        products = product.favorite_product.split(',')
        
        data = []
        
        for item in products:
            data.append(get_product_id(item))
        
        return jsonify(data),200
    
    except:
        return jsonify({"message":"internal error"}),500



def get_all_product():
    """
    This function retrieves all products and returns them as a JSON object, with error handling for
    internal errors.
    :return: a JSON response with either a list of all products and a status code of 200, or a message
    indicating an internal error and a status code of 500.
    """
    
    try:
        products = All_product()
    
        return jsonify(products),200
    
    except:
        return jsonify({"message":"internal error"}),500