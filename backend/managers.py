from flask import Blueprint, jsonify, request

managers = []
next_id = 1

managers_bp = Blueprint('managers', __name__)

@managers_bp.route('/managers', methods=['GET'])
def get_managers():
    return jsonify(managers)

@managers_bp.route('/managers', methods=['POST'])
def add_manager():
    global next_id
    manager_data = request.json
    new_manager = {
        "id": next_id,
        "name": manager_data["name"],
        "age": manager_data["age"]
    }
    managers.append(new_manager)
    next_id += 1
    return jsonify(new_manager), 201

@managers_bp.route('/managers/<int:manager_id>', methods=['PUT'])
def update_manager(manager_id):
    manager_data = request.json
    manager = next((s for s in managers if s["id"] == manager_id), None)
    if not manager:
        return jsonify({"error": "manager not found"}), 404
    manager.update({"name": manager_data["name"], "age": manager_data["age"]})
    return jsonify(manager)

@managers_bp.route('/managers/<int:manager_id>', methods=['DELETE'])
def delete_manager(manager_id):
    global managers
    managers = [s for s in managers if s["id"] != manager_id]
    return '', 204
