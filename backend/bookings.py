from flask import Blueprint, jsonify, request

bookings = []
next_id = 1

bookings_bp = Blueprint('bookings', __name__)

@bookings_bp.route('/bookings', methods=['GET'])
def get_bookings():
    return jsonify(bookings)

@bookings_bp.route('/bookings', methods=['POST'])
def add_booking():
    global next_id
    booking_data = request.json
    new_booking = {
        "id": next_id,
        "name": booking_data["name"],
        "age": booking_data["age"]
    }
    bookings.append(new_booking)
    next_id += 1
    return jsonify(new_booking), 201

@bookings_bp.route('/bookings/<int:booking_id>', methods=['PUT'])
def update_booking(booking_id):
    booking_data = request.json
    booking = next((s for s in bookings if s["id"] == booking_id), None)
    if not booking:
        return jsonify({"error": "booking not found"}), 404
    booking.update({"name": booking_data["name"], "age": booking_data["age"]})
    return jsonify(booking)

@bookings_bp.route('/bookings/<int:booking_id>', methods=['DELETE'])
def delete_booking(booking_id):
    global bookings
    bookings = [s for s in bookings if s["id"] != booking_id]
    return '', 204
