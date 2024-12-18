from flask import Blueprint, jsonify, request
from db_cursor import select_records, insert_new_record

#ID, NAME, IDPLACE
table_name = "trips"
trips = select_records(table_name)

def get_trip_from_DB(trip_id):
    return select_records(table_name, trip_id)

print(trips)
next_id = trips[-1][0] + 1 

trips_bp = Blueprint('trips', __name__)

@trips_bp.route('/trips', methods=['GET'])
def get_trips():
    return jsonify(trips)

@trips_bp.route('/trips/<int:trip_id>', methods=['GET'])
def get_trip(trip_id):
    return jsonify(trips[trip_id])

@trips_bp.route('/trips', methods=['POST'])
def add_trip():
    trip_data = request.json
    new_trip = {
        "name": trip_data["name"],
        "idplace": trip_data["idplace"]
    }
    insert_new_record(table_name, new_trip)
    next_id += 1
    trips.append(get_trip_from_DB(next_id))
    return jsonify(new_trip), 201

@trips_bp.route('/trips/<int:trip_id>', methods=['PUT'])
def update_trip(trip_id):
    trip_data = request.json
    trip = next((s for s in trips if s["id"] == trip_id), None)
    if not trip:
        return jsonify({"error": "trip not found"}), 404
    trip.update({"name": trip_data["name"], "idplace": trip_data["idplace"]})
    return jsonify(trip)

@trips_bp.route('/trips/<int:trip_id>', methods=['DELETE'])
def delete_trip(trip_id):
    global trips
    trips = [s for s in trips if s["id"] != trip_id]
    return '', 204
