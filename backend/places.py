from flask import Blueprint, jsonify, request
from db_cursor import select_records, insert_new_record, get_last_id, update_row_in_table, delete_row_from_table

table_name = "places"

def get_place_from_DB(place_id=None):
    records = select_records(table_name, place_id)
    result = []
    for record in records:
        record_dict = {
            'id': record[0],
            'name': record[1],
            'country': record[2],
            'coordinates': record[3],
            'description': record[4]
        }
        result.append(record_dict)
    return result

places_bp = Blueprint('places', __name__)

@places_bp.route('/places', methods=['GET'])
def get_places():
    return jsonify(get_place_from_DB())

@places_bp.route('/places/<int:place_id>', methods=['GET'])
def get_place(place_id):
    return jsonify(get_place_from_DB(place_id))

@places_bp.route('/places', methods=['POST'])
def add_place():
    global next_id
    place_data = request.json
    new_place = {
        "name": place_data["name"],
        "country": place_data["country"],
        "coordinates": place_data["coordinates"],
        "description": place_data["description"]
    }
    insert_new_record(table_name, new_place)
    created_place = get_place_from_DB(get_last_id(table_name))[0]
    return jsonify(created_place), 201

@places_bp.route('/places/<int:place_id>', methods=['PUT'])
def update_place(place_id):
    place_data = request.json
    places = get_place_from_DB()
    place = next((s for s in places if s[0] == place_id), None)
    if not place:
        return jsonify({"error": "place not found"}), 404
    update_row_in_table(
        table_name,
        place_id,
        {
            "name": place_data["name"],
            "country": place_data["country"],
            "coordinates": place_data["coordinates"],
            "description": place_data["description"]
        }
    )
    return jsonify(get_place_from_DB(place_id))

@places_bp.route('/places/<int:place_id>', methods=['DELETE'])
def delete_place(place_id):
    delete_row_from_table(table_name, place_id)
    return '', 204
