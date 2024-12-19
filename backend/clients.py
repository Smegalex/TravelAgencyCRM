from flask import Blueprint, jsonify, request
from db_cursor import select_records, insert_new_record, get_last_id, update_row_in_table, delete_row_from_table

table_name = "clients"


def get_client_from_DB(client_id=None):
    return select_records(table_name, client_id)


clients_bp = Blueprint('clients', __name__)


@clients_bp.route('/clients', methods=['GET'])
def get_clients():
    return jsonify(get_client_from_DB())


@clients_bp.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    return jsonify(get_client_from_DB(client_id))


@clients_bp.route('/clients', methods=['POST'])
def add_client():
    global next_id
    client_data = request.json
    new_client = {
        "name": client_data["name"],
        "surname": client_data["surname"],
        "email": client_data["email"]
    }
    insert_new_record(table_name, new_client)
    created_client = get_client_from_DB(get_last_id(table_name))[0]
    return jsonify(created_client), 201


@clients_bp.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    client_data = request.json
    clients = get_client_from_DB()
    client = next((s for s in clients if s[0] == client_id), None)
    print(client)
    if not client:
        return jsonify({"error": "client not found"}), 404
    update_row_in_table(table_name, client_id, {"name": client_data["name"],
                                                "surname": client_data["surname"],
                                                "email": client_data["email"]})
    return jsonify(get_client_from_DB(client_id))


@ clients_bp.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    delete_row_from_table(table_name, client_id)
    return '', 204
