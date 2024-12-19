from flask import Blueprint, jsonify, request
from db_cursor import select_records, insert_new_record, get_last_id, update_row_in_table, delete_row_from_table

table_name = "bookings"

def get_booking_from_DB(booking_id=None):
    return select_records(table_name, booking_id)

bookings_bp = Blueprint('bookings', __name__)

@bookings_bp.route('/bookings', methods=['GET'])
def get_bookings():
    return jsonify(get_booking_from_DB())

@bookings_bp.route('/bookings/<int:booking_id>', methods=['GET'])
def get_booking(booking_id):
    return jsonify(get_booking_from_DB(booking_id))

@bookings_bp.route('/bookings', methods=['POST'])
def add_booking():
    global next_id
    booking_data = request.json
    new_booking = {
        "idclient": booking_data["idclient"],
        "idmanager": booking_data["idmanager"],
        "idtrip": booking_data["idtrip"],
        "people_amount": booking_data["people_amount"]
    }
    insert_new_record(table_name, new_booking)
    created_booking = get_booking_from_DB(get_last_id(table_name))[0]
    return jsonify(created_booking), 201

@bookings_bp.route('/bookings/<int:booking_id>', methods=['PUT'])
def update_booking(booking_id):
    booking_data = request.json
    bookings = get_booking_from_DB()
    booking = next((s for s in bookings if s[0] == booking_id), None)
    print(booking)
    if not booking:
        return jsonify({"error": "booking not found"}), 404
    update_row_in_table(table_name, booking_id, {"name": booking_data["name"], "idplace": booking_data["idplace"]})
    return jsonify(get_booking_from_DB(booking_id))

@bookings_bp.route('/bookings/<int:booking_id>', methods=['DELETE'])
def delete_booking(booking_id):
    delete_row_from_table(table_name, booking_id)
    return '', 204
