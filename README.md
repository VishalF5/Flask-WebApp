# Flask MongoDB CRUD API

This project is a Flask application that provides a RESTful API for performing CRUD (Create, Read, Update, Delete) operations on a User resource stored in a MongoDB database. The application is containerized using Docker.

## Features

- RESTful API with endpoints for managing users.
- User resource with fields: `id`, `name`, `email`, and `password`.
- Containerized using Docker and Docker Compose.


## Installation

### Prerequisites

- Docker
- Docker Compose

### Steps to Set Up

1. **Clone the Repository**

   ```bash
   git clone https://github.com/VishalF5/Flask-WebApp.git
   cd Flask-WebApp
    ```

2. **Build and Start Containers**
    ```bash
    docker-compose up --build -d
    ```

3. **Access API's**

    The API will be available at ``` http://localhost:5000 ```


## API Endpoints

### Create User

- **Endpoint:** `POST /users`
- **Description:** Creates a new user.
- **Request Body:**
  ```json
  {
    "name": "Vishal",
    "email": "vishal@mail.com",
    "password": "pass"
  }
  ```
- **Example** 
    ```bash
    curl -XPOST --insecure "http://localhost:5000/users" -H 'Content-Type: application/json' -d '{
        "name": "Vishal",
        "email": "vishal@mail.com",
        "password": "pass"
    }'
    ```
- **Response**
    ```json
        {
        "id": "unique_user_id",
        "name": "Vishal",
        "email": "vishal@mail.com",
        }
    ```

### Get All Users

- **Endpoint**: `GET /users`
- **Description**: Retrieves a list of all users.



### Get User by ID

- **Endpoint**: `GET /users/<id>`
- **Description**: Retrieves a user by their unique ID.


### Update User by ID

- **Endpoint**: `PUT /users/<id>`
- **Description**: Updates an existing user by their unique ID.


### Delete User by ID

- **Endpoint**: `DELETE /users/<id>`
- **Description**: Deletes a user by their unique ID.
