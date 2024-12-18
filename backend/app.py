from flask import Flask
from flask_cors import CORS

from managers import managers_bp
from clients import clients_bp
from places import places_bp
from bookings import bookings_bp
from trips import trips_bp
from db_cursor import get_db_cursor

conn, cursor = get_db_cursor()
cursor.execute("SELECT Table_name FROM user_tables")
for row in cursor:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()



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