from flask import Blueprint, jsonify, request

places = []
next_id = 1

places_bp = Blueprint('places', __name__)

@places_bp.route('/places', methods=['GET'])
def get_places():
    return jsonify(places)

@places_bp.route('/places', methods=['POST'])
def add_place():
    global next_id
    place_data = request.json
    new_place = {
        "id": next_id,
        "name": place_data["name"],
        "age": place_data["age"]
    }
    places.append(new_place)
    next_id += 1
    return jsonify(new_place), 201

@places_bp.route('/places/<int:place_id>', methods=['PUT'])
def update_place(place_id):
    place_data = request.json
    place = next((s for s in places if s["id"] == place_id), None)
    if not place:
        return jsonify({"error": "place not found"}), 404
    place.update({"name": place_data["name"], "age": place_data["age"]})
    return jsonify(place)

@places_bp.route('/places/<int:place_id>', methods=['DELETE'])
def delete_place(place_id):
    global places
    places = [s for s in places if s["id"] != place_id]
    return '', 204
