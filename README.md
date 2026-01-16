# Late Show API

**Author:** James Kisengi

## Description

The Late Show API is a Flask-based RESTful API that models episodes of a late-night show, their guests, and guest appearances. It demonstrates relational database design, data validation, and RESTful routing using Flask, SQLAlchemy, and Flask-Migrate.

This project fulfills the Phase 4 backend requirements by implementing database models, relationships, validations, migrations, seed data, and API endpoints that return properly structured JSON responses.

## Technologies Used

- Python 3.8
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLAlchemy Serializer
- SQLite
- Postman (for API testing)

## Database Models & Relationships

### Models

- **Episode**: Represents a show episode with date and number.
- **Guest**: Represents a guest with name and occupation.
- **Appearance**: Represents a guest's appearance on an episode with a rating.

### Relationships

- An Episode has many Guests through Appearances
- A Guest has many Episodes through Appearances
- An Appearance belongs to one Episode and one Guest
- Cascade deletes are enabled to maintain database integrity.

### Validations

- Appearance rating must be between 1 and 5 (inclusive).

## Setup Instructions

1. Clone the repository.
2. Navigate to the project directory.
3. Install dependencies: `pip install -r requirements.txt`
4. Navigate to the server directory: `cd server`
5. Run migrations: `flask db upgrade`
6. Seed the database: `python seed.py`
7. Run the application: `flask run`

## API Endpoints

### GET /episodes
Returns a list of all episodes.

**Response:**
```json
[
  {
    "id": 1,
    "date": "1/11/99",
    "number": 1
  },
  {
    "id": 2,
    "date": "1/12/99",
    "number": 2
  }
]
```

### GET /episodes/:id
Returns details of a specific episode including appearances.

**Response (Success):**
```json
{
  "id": 1,
  "date": "1/11/99",
  "number": 1,
  "appearances": [
    {
      "id": 1,
      "episode_id": 1,
      "guest_id": 1,
      "rating": 4,
      "guest": {
        "id": 1,
        "name": "Michael J. Fox",
        "occupation": "actor"
      }
    }
  ]
}
```

**Response (Not Found):**
```json
{
  "error": "Episode not found"
}
```

### GET /guests
Returns a list of all guests.

**Response:**
```json
[
  {
    "id": 1,
    "name": "Michael J. Fox",
    "occupation": "actor"
  },
  {
    "id": 2,
    "name": "Sandra Bernhard",
    "occupation": "comedian"
  }
]
```

### POST /appearances
Creates a new appearance.

**Request Body:**
```json
{
  "rating": 5,
  "episode_id": 100,
  "guest_id": 123
}
```

**Response (Success):**
```json
{
  "id": 162,
  "rating": 5,
  "guest_id": 3,
  "episode_id": 2,
  "episode": {
    "date": "1/12/99",
    "id": 2,
    "number": 2
  },
  "guest": {
    "id": 3,
    "name": "Tracey Ullman",
    "occupation": "television actress"
  }
}
```

**Response (Error):**
```json
{
  "errors": ["validation errors"]
}
```

## Testing

Import the provided Postman collection (`challenge-4-lateshow.postman_collection.json`) into Postman to test the API endpoints.
