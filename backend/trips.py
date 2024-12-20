from flask import Blueprint, jsonify, request
from db_cursor import select_records, insert_new_record, get_last_id, update_row_in_table, delete_row_from_table

table_name = "trips"

def get_trip_from_DB(trip_id=None):
    records = select_records(table_name, trip_id)
    result = []
    for record in records:
        record_dict = {
            'id': record[0],
            'name': record[1],
            'idplace': record[2],
            'season': record[3]
        }
        result.append(record_dict)
    return result


trips_bp = Blueprint('trips', __name__)


@trips_bp.route('/trips', methods=['GET'])
def get_trips():
    return jsonify(get_trip_from_DB())


@trips_bp.route('/trips/<int:trip_id>', methods=['GET'])
def get_trip(trip_id):
    return jsonify(get_trip_from_DB(trip_id))


@trips_bp.route('/trips', methods=['POST'])
def add_trip():
    global next_id
    trip_data = request.json
    new_trip = {
        "name": trip_data["name"],
        "idplace": trip_data["idplace"]
    }
    insert_new_record(table_name, new_trip)
    created_trip = get_trip_from_DB(get_last_id(table_name))[0]
    return jsonify(created_trip), 201


@trips_bp.route('/trips/<int:trip_id>', methods=['PUT'])
def update_trip(trip_id):
    trip_data = request.json
    trips = get_trip_from_DB()
    trip = next((s for s in trips if s[0] == trip_id), None)
    print(trip)
    if not trip:
        return jsonify({"error": "trip not found"}), 404
    update_row_in_table(table_name, trip_id, {
                        "name": trip_data["name"], "idplace": trip_data["idplace"]})
    return jsonify(get_trip_from_DB(trip_id))


@trips_bp.route('/trips/<int:trip_id>', methods=['DELETE'])
def delete_trip(trip_id):
    delete_row_from_table(table_name, trip_id)
    return '', 204
