from flask import Flask
from flask_cors import CORS
from flask import session

from managers import managers_bp
from clients import clients_bp
from places import places_bp
from bookings import bookings_bp
from trips import trips_bp
from login import login_bp

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.config.update(
    SESSION_COOKIE_HTTPONLY = False
)

app.config['SESSION_COOKIE_SAMESITE'] = 'None'
app.config['SESSION_COOKIE_SECURE'] = True

app.secret_key = b'_5#y2kL"F4Q8z\n\xec]/'

# Реєстрація Blueprints
app.register_blueprint(managers_bp)
app.register_blueprint(clients_bp)
app.register_blueprint(places_bp)
app.register_blueprint(bookings_bp)
app.register_blueprint(trips_bp)
app.register_blueprint(login_bp)

@app.route('/')
def index():
    if 'username' and 'rights' in session:
        print(f'Logged in as {session["username"]} with rights {session["rights"]}')
        return f'Logged in as {session["username"]} with rights {session["rights"]}'
    return 'You are not logged in'

if __name__ == '__main__':
    app.run(debug=True)