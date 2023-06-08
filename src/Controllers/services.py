from flask import request, jsonify
from dotenv import load_dotenv
from functools import wraps

import os

load_dotenv()

def auth(void):
    """
    This is a Python function that decorates another function with authentication logic using a token
    and an environment variable.
    
    :param void: `void` is a function that will be decorated by the `auth` function. It is a placeholder
    for any function that needs to be authenticated before it can be executed
    :return: The function `decorated` is being returned, which is a decorator function that checks if
    the `token` provided in the request headers matches the `AUTH` key stored in the environment
    variables. If the tokens do not match, a JSON response with a 401 status code is returned. If the
    tokens match, the original function passed as an argument to `auth` is called with the provided
    arguments
    """
    @wraps(void)
    def decorated(*args, **kwargs):
        token = request.headers.get('token')
        
        

        key = os.getenv('AUTH')
        print(key)
        if token != key:
            return jsonify({'message': 'Acesso não autorizado'}), 401

        return void(*args, **kwargs)

    return decorated