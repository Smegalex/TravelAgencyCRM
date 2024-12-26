from flask import Blueprint, request, jsonify
from flask import session
from db_cursor import check_user_credentials
from managers import get_manager_id_by_email, get_manager


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
        session['username'] = email
        mng_id = get_manager_id_by_email(email)
        session['rights'] = get_manager(mng_id).json[0]['adminRights']
        session['userId'] = mng_id
        print("login success")
        return jsonify({"success": True, "message": "Login successful"}), 200
    else:
        return jsonify({"success": False, "message": "Invalid credentials"}), 401


@login_bp.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('adminRights', None)
    session.pop('userId', None)
    return "Logged out successfully", 200
    # return redirect(url_for('index'))


@login_bp.route('/session/username', methods=['GET'])
def get_username():
    try:
        if session['username']:
            return jsonify(session['username'])
        else:
            return jsonify(None)
    except KeyError:
        return jsonify(None)


@login_bp.route('/session/adminRights', methods=['GET'])
def get_rights():
    try:
        if session['rights']:
            return jsonify(session['rights'])
        else:
            return jsonify(None)
    except KeyError:
        return jsonify(None)


@login_bp.route('/session/userId', methods=['GET'])
def get_id():
    try:
        if session['userId']:
            return jsonify(session['userId'])
        else:
            return jsonify(None)
    except KeyError:
        return jsonify(None)

# @login_bp.route('/debug', methods=['GET'])
# def debug():
#     return jsonify(request.cookies)
