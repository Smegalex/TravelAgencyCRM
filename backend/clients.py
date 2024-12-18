from flask import Blueprint, jsonify, request

clients = []
next_id = 1

clients_bp = Blueprint('clients', __name__)

@clients_bp.route('/clients', methods=['GET'])
def get_clients():
    return jsonify(clients)

@clients_bp.route('/clients', methods=['POST'])
def add_client():
    global next_id
    client_data = request.json
    new_client = {
        "id": next_id,
        "name": client_data["name"],
        "age": client_data["age"]
    }
    clients.append(new_client)
    next_id += 1
    return jsonify(new_client), 201

@clients_bp.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    client_data = request.json
    client = next((s for s in clients if s["id"] == client_id), None)
    if not client:
        return jsonify({"error": "client not found"}), 404
    client.update({"name": client_data["name"], "age": client_data["age"]})
    return jsonify(client)

@clients_bp.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    global clients
    clients = [s for s in clients if s["id"] != client_id]
    return '', 204
