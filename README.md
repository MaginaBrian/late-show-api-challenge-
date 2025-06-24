# late-show-api-challenge-


🌙 Late Show API Challenge

A RESTful API for managing a Late Night TV show system, built with Flask, SQLAlchemy, Flask-Migrate, and Flask-JWT-Extended using the MVC architecture and PostgreSQL.

🚀 Features


Register and login users with JWT-based authentication
List all episodes
View an episode with its guest appearances
Delete an episode (and its appearances, with cascade delete)
List all guests
Create a guest appearance on an episode (authenticated)

🛠 Technologies Used

Python 3.12
Flask
Flask-SQLAlchemy
Flask-Migrate
Flask-JWT-Extended
PostgreSQL
Postman

📁 Project Structure
.
├── server/
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── seed.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── guest.py
│   │   ├── episode.py
│   │   ├── appearance.py
├── controllers/
│   ├── __init__.py
│   ├── auth_controller.py
│   ├── guest_controller.py
│   ├── episode_controller.py
│   ├── appearance_controller.py
├── migrations/
├── challenge-4-lateshow.postman_collection.json
├── README.md


⚙️ Setup Instructions

Clone the repository:
git clone https://github.com/your-username/late-show-api-challenge.git
cd late-show-api-challenge


Set up virtual environment:
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
pipenv shell


Set up PostgreSQL database:

Ensure PostgreSQL is installed and running.
Create the database:CREATE DATABASE late_show_db;


Set environment variables for secure configuration:export DATABASE_URL="postgresql://<your-username>:<your-password>@localhost:5432/late_show_db"
export JWT_SECRET_KEY="your-secure-secret-key"

Replace <your-username>, <your-password>, and your-secure-secret-key with your PostgreSQL credentials and a strong JWT secret key.


Set Flask app:

export FLASK_APP=server.app


Run migrations:

flask db init
flask db migrate -m "Initial migration"
flask db upgrade


Seed the database:

python server/seed.py


Run the server:

flask run



 Authentication Flow

Register: Create a user with a unique username and password via POST /register.
Login: Authenticate with username and password via POST /login to receive a JWT token.
Protected Routes: Include the JWT token in the Authorization header as Bearer <token> for:
POST /appearances
DELETE /episodes/<id>


📬 API Endpoints



Method       Endpoint          Auth Required?           Description

POST         /Register             No               Register a new user

POST         /LOGIN                No               Login and receive JWT token

GET          /EPISODES             NO               List all episodes

GET          /EPISODES/<id>        No               Get episode details with appearances

DELETE       /EPISODES/<id>        Yes              Delete an episode and its appearances

GET          /GUESTS               No               List all guests

POST         /APPEARANCES          Yes              Create a guest appearance


Postman Usage Guide

Import the Postman collection:

Download challenge-4-lateshow.postman_collection.json.

In Postman, go to File > Import and select the file.

Test unauthenticated routes:

Send GET /episodes, GET /episodes/<id>, and GET /guests without headers.

Send POST /register and POST /login with JSON bodies (see sample requests).

Test authenticated routes:

After POST /login, copy the access_token from the response.

For POST /appearances and DELETE /episodes/<id>, add a header:

Key: Authorization

Value: Bearer <access_token>

Verify responses match the expected status codes and formats (see sample responses).


📌 GitHub Repository

https://github.com/your-username/late-show-api-challenge

Replace your-username with your actual GitHub username.