from flask import Blueprint, jsonify, request
from db_cursor import select_records, insert_new_record, get_last_id, update_row_in_table, delete_row_from_table

table_name = "managers"


def get_manager_from_DB(manager_id=None):
    records = select_records(table_name, manager_id)
    result = []
    for record in records:
        record_dict = {
            'id': record[0],
            'name': record[1],
            'surname': record[2],
            'email': record[3],
            'adminRights': bool(record[4]),
            'password': record[5]
        }
        result.append(record_dict)
    return result


managers_bp = Blueprint('managers', __name__)


@managers_bp.route('/managers', methods=['GET'])
def get_managers():
    return jsonify(get_manager_from_DB())


@managers_bp.route('/managers/<int:manager_id>', methods=['GET'])
def get_manager(manager_id):
    return jsonify(get_manager_from_DB(manager_id))


@managers_bp.route('/managers', methods=['POST'])
def add_manager():
    global next_id
    manager_data = request.json
    new_manager = {
        "name": manager_data["name"],
        "surname": manager_data["surname"],
        "email": manager_data["email"],
        "adminRights": manager_data["adminRights"],
        "password": manager_data["password"]
    }
    insert_new_record(table_name, new_manager)
    created_manager = get_manager_from_DB(get_last_id(table_name))[0]
    return jsonify(created_manager), 201


@managers_bp.route('/managers/<int:manager_id>', methods=['PUT'])
def update_manager(manager_id):
    password_bool = request.args.get('password')
    manager_data = request.json
    managers = get_manager_from_DB()
    manager = next((s for s in managers if s['id'] == manager_id), None)
    print(manager)
    if not manager:
        return jsonify({"error": "manager not found"}), 404
    if password_bool:
        update_row_in_table(table_name, manager_id, {"name": manager_data["name"],
                                                 "surname": manager_data["surname"],
                                                 "email": manager_data["email"],
                                                 "adminRights": manager_data["adminRights"],
                                                 "password": manager_data["password"]})
    else:
        update_row_in_table(table_name, manager_id, {"name": manager_data["name"],
                                                     "surname": manager_data["surname"],
                                                     "email": manager_data["email"],
                                                     "adminRights": manager_data["adminRights"]})
    return jsonify(get_manager_from_DB(manager_id))


@managers_bp.route('/managers/<int:manager_id>', methods=['DELETE'])
def delete_manager(manager_id):
    delete_row_from_table(table_name, manager_id)
    return '', 204
