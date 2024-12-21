from flask import Blueprint, request, jsonify
from db_cursor import check_user_credentials

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    """
    Обробляє запит на логін.
    """
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not login or not password:
        return jsonify({"success": False, "message": "Email and password are required"}), 400

    # Виклик функції перевірки облікових даних
    is_valid_user = check_user_credentials(email, password)

    if is_valid_user:
        return jsonify({"success": True, "message": "Login successful"}), 200
    else:
        return jsonify({"success": False, "message": "Invalid credentials"}), 401
