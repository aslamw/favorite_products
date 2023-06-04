from flask import Blueprint, request, jsonify
from ..Models import db, Client

api_client = Blueprint('client', __name__)

@api_client.post("/clients")
def create_client():
    
    pass


@api_client.put("/clients/<int:client_id>")
def update_client(client_id):
    
    pass


@api_client.get("/clients/<int:client_id>")
def get_client(client_id):
    
    pass


@api_client.delete("/clients/<int:client_id>")
def delete_client(client_id):
    
    pass
