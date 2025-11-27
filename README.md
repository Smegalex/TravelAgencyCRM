# Travel Agency CRM

A Customer Relationship Management (CRM) system designed for an imaginary travel agency. This full-stack application allows travel agencies to manage clients, bookings, trips, and agency managers efficiently.

## Technologies Used

### Frontend
- **Vue.js 3** - Progressive JavaScript framework for building user interfaces
- **Vue Router** - Official router for Vue.js
- **Pinia** - State management for Vue.js
- **PrimeVue** - Rich UI component library for Vue.js
- **Vite** - Fast build tool and development server
- **Font Awesome** - Icon library
- **Vee-Validate & Yup** - Form validation

### Backend
- **Flask** - Python web framework for the REST API
- **Flask-CORS** - Cross-Origin Resource Sharing support
- **Oracle Database** - Relational database for data persistence

## Features

- **Client Management** - Create, view, edit, and delete client records
- **Trip Management** - Manage travel trips with destination information
- **Booking System** - Create and manage bookings linking clients to trips
- **Manager Administration** - Admin users can manage other managers
- **Authentication** - Session-based login system with role-based access control
- **Responsive UI** - Modern interface with PrimeVue components

## Project Structure

```
TravelAgencyCRM/
├── frontend/               # Vue.js frontend application
│   ├── src/
│   │   ├── components/     # Reusable Vue components
│   │   ├── pages/          # Page components
│   │   │   ├── tables/     # CRUD table views
│   │   │   ├── detailed/   # Detailed record views
│   │   │   ├── modals/     # Modal dialogs
│   │   │   └── service/    # Service pages (login, errors)
│   │   ├── requests/       # API request modules
│   │   ├── stores/         # Pinia state stores
│   │   ├── styles/         # Global styles
│   │   ├── router.js       # Vue Router configuration
│   │   └── App.vue         # Root component
│   ├── package.json        # Frontend dependencies
│   └── vite.config.js      # Vite configuration
├── backend/                # Flask backend API
│   ├── app.py              # Flask application entry point
│   ├── clients.py          # Clients API endpoints
│   ├── trips.py            # Trips API endpoints
│   ├── bookings.py         # Bookings API endpoints
│   ├── managers.py         # Managers API endpoints
│   ├── places.py           # Places API endpoints
│   ├── login.py            # Authentication endpoints
│   └── db_cursor.py        # Database connection utility
└── DB/
    └── TravelCRM.sql       # Database schema
```

## Database Schema

The application uses an Oracle database with the following tables:

- **Managers** - Agency staff with admin rights management
- **Clients** - Customer information
- **Trips** - Travel packages with destination references
- **Places** - Destination locations with coordinates and descriptions
- **Bookings** - Links clients, trips, and managers with party size

## Getting Started

### Prerequisites

- Node.js (v18 LTS or higher)
- Python 3.x
- Oracle Database

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

The development server will start at `http://localhost:5173`

### Backend Setup

```bash
cd backend
pip install flask flask-cors oracledb
python app.py
```

The Flask API will run at `http://localhost:5000`

### Database Setup

1. Execute the SQL script in `DB/TravelCRM.sql` to create the database schema
2. Configure database connection settings in `backend/db_cursor.py`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/POST | `/clients` | List or create clients |
| GET/PUT/DELETE | `/clients/:id` | Get, update, or delete a client |
| GET/POST | `/trips` | List or create trips |
| GET/PUT/DELETE | `/trips/:id` | Get, update, or delete a trip |
| GET/POST | `/bookings` | List or create bookings |
| GET/PUT/DELETE | `/bookings/:id` | Get, update, or delete a booking |
| GET | `/clients/:id/bookings` | Get bookings for a specific client |
| GET/POST | `/managers` | List or create managers |
| GET/PUT/DELETE | `/managers/:id` | Get, update, or delete a manager |
| GET/POST | `/places` | List or create places |
| GET/PUT/DELETE | `/places/:id` | Get, update, or delete a place |
| POST | `/login` | Authenticate user |
| GET | `/logout` | End user session |

## License

This project was created for educational purposes.
