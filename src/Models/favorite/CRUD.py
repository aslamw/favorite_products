from .table import Favorite_Product, favorite_schema, db, favorites_schema
    
    
    
def exist_or_get_favorite(value):
    """
    This function checks if a favorite product exists for a given client ID and returns it if it does,
    otherwise it returns None.
    
    :param value: The value parameter is the client ID that is being used to search for a favorite
    product in the database
    :return: The function `exist_or_get_favorite` returns either a `Favorite_Product` object if it
    exists in the database with a `client_id` matching the input `value`, or `None` if it does not
    exist.
    """
    
    favorite = Favorite_Product.query.filter(Favorite_Product.client_id == value).first()

    
    if favorite is not None:
        return favorite
    
    
    return None
    

def create_favorite(id, produto_id):
    """
    This function creates a favorite product object for a given client ID and product ID.
    
    :param id: The id parameter is likely a unique identifier for a client or user. It is used to create
    a new Favorite_Product object for that specific client
    :param produto_id: The parameter "produto_id" is likely an identifier for a specific product that a
    user wants to add to their list of favorite products
    :return: an instance of the `Favorite_Product` class with the `client_id` set to the `id` parameter
    and the `favorite_product` set to the string representation of the `produto_id` parameter.
    """
    
    product_F = Favorite_Product(client_id=id, favorite_product=str(produto_id))

    return product_F



def update_favorite(product, product_id):
    """
    This function updates a product's favorite list by adding a new product ID to it.
    
    :param product: The product object that needs to be updated with a new favorite product ID
    :param product_id: The product_id parameter is the unique identifier of a product in the database.
    It is used to identify the product that the user wants to add to their favorites list
    :return: a response object that contains the updated favorite product list for the given product.
    """
    
    favorite = product.favorite_product.split(',')
    
    if product_id in favorite:
        return False
    
    favorite.append(str(product_id))
    product.favorite_product = ','.join(favorite)
    
    db.session.commit()
    
    response = favorite_schema.dump(product)
    
    return response



def delete_favorite(product, product_id):
    """
    This function deletes a product from a user's list of favorite products.
    
    :param product: The product object that needs to have a favorite product removed from its list of
    favorites
    :param product_id: The product_id parameter is the unique identifier of the product that the user
    wants to remove from their favorites list
    :return: a response in the form of a serialized JSON object of the updated product after removing
    the specified product_id from its list of favorite products. If the product_id is not found in the
    list, it returns False.
    """
    
    favorite = product.favorite_product.split(',')
    
    if product_id not in favorite:
        return False
    
    favorite.remove(str(product_id))
    product.favorite_product = ','.join(favorite)
    
    db.session.commit()
    
    response = favorite_schema.dump(product)
    
    return response



def All_product():
    """
    This function retrieves all favorite products and returns them as a response.
    :return: a response object that contains a serialized representation of all the favorite products in
    the database.
    """
    
    product = Favorite_Product.query.all()
    
    response = favorites_schema.dump(product)
    
    return response