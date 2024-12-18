from flask import Flask
from flask_cors import CORS

from managers import managers_bp
from clients import clients_bp
from places import places_bp
from bookings import bookings_bp
from trips import trips_bp

app = Flask(__name__)
CORS(app)

# Реєстрація Blueprints
app.register_blueprint(managers_bp)
app.register_blueprint(clients_bp)
app.register_blueprint(places_bp)
app.register_blueprint(bookings_bp)
app.register_blueprint(trips_bp)

if __name__ == '__main__':
    app.run(debug=True)