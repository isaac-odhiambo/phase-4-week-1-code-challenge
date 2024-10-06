# phase-4-week-1-code-challenge
# Superheroes API

## Overview
This is a Flask API for managing superheroes, their powers, and the relationships between them.



Superheroes API
Overview
This is a Flask-based API for managing superheroes, their powers, and the relationships between them. The API supports CRUD operations and utilizes SQLAlchemy for ORM functionality.

Technologies Used
Flask: A micro web framework for Python, essential for building the API.
Flask-Migrate: Handles SQLAlchemy database migrations for version control.
Flask-CORS: Enables Cross-Origin Resource Sharing, allowing the API to be accessed from different domains.
SQLAlchemy: ORM that provides a high-level abstraction for database interactions.
SQLAlchemy-Serializer: Helps with serializing SQLAlchemy models to JSON format.
Faker: Generates fake data for seeding the database, useful during development and testing.
Python: The programming language used for developing the application.
Author
Name: Your Name
GitHub: Your GitHub Profile
Models
1. Hero
Attributes:
id: Unique identifier for each hero.
name: Name of the hero.
super_name: Hero's superhero alias.
Relationships:
A hero can have many powers through the HeroPower join table.
2. Power
Attributes:
id: Unique identifier for each power.
name: Name of the power.
description: Detailed description of what the power does.
Validations:
description must be at least 20 characters long.
3. HeroPower
Attributes:
id: Unique identifier for each relationship.
hero_id: Foreign key referencing the Hero.
power_id: Foreign key referencing the Power.
strength: Level of strength associated with the hero's power.
Validations:
strength must be one of the following values: 'Strong', 'Weak', 'Average'.
Relationships:
Belongs to both Hero and Power.
Dependencies
The project requires the following dependencies:

Flask
Flask-Migrate
Flask-CORS
SQLAlchemy
SQLAlchemy-Serializer
Faker
Installing Dependencies
To install the required dependencies, run:

## Running the API
Set Up the Database: Make sure your database is set up and migrations are applied. Run:


flask db upgrade
Seed the Database: Populate the database with initial data by running:


python seed.py
Run the Flask Application: Start the Flask development server with:


python app.py
Access the API: The API will be accessible at http://127.0.0.1:5555. You can test the endpoints using tools like Postman or cURL.

API Endpoints
1. GET /heroes
Returns a list of all heroes.

2. GET /heroes/
Returns detailed information about a specific hero, including their powers.

3. GET /powers
Returns a list of all powers.

4. GET /powers/
Returns detailed information about a specific power.

5. PATCH /powers/
Updates an existing power's description.

6. POST /hero_powers
Creates a new relationship between a hero and a power.

Conclusion
This API serves as a comprehensive solution for managing superheroes and their abilities. It allows for easy expansion and modification, making it a valuable tool for developers interested in building superhero-related applications.

Feel free to reach out for any questions or suggestions!



## Testing
Use Postman to test the API endpoints using the provided Postman collection.

## License
This project is licensed under the MIT License.
