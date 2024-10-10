# Flask MongoDB CRUD API

This project is a Flask application that provides a RESTful API for an assignment submission portal. The application is containerized using Docker.

## Features

- RESTful API with endpoints for managing users.
- User resource with fields: `id`, `name` and `password`.
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

- **Endpoint:** `POST /register`
- **Description:** Creates a new user.
- **Request Body:**
  ```json
  {
    "name": "Vishal",
    "password": "pass"
  }
  ```
- **Example** 
    ```bash
    curl -XPOST --insecure "http://localhost:5000/register" -H 'Content-Type: application/json' -d '{
        "username": "Vishal",
        "password": "pass"
    }'
    ```
- **Response**
    ```json
        {
            "message": "User registered successfully."
        }
    ```


### Create an Admin User

- **Endpoint:** `POST /admin/register`
- **Description:** Creates a new admin user.
- **Request Body:**
  ```json
  {
    "name": "Vishal",
    "password": "pass"
  }
  ```
- **Example** 
    ```bash
    curl -XPOST --insecure "http://localhost:5000/admin/register" -H 'Content-Type: application/json' -d '{
        "username": "Vishal",
        "password": "pass"
    }'
    ```
- **Response**
    ```json
        {
            "message": "Admin registered successfully."
        }
    ```

### Get All Admins

- **Endpoint**: `GET /admins`
- **Description**: Retrieves a list of all admins.
- **Example** 
    ```bash
    curl -XGET --insecure "http://localhost:5000/admins"
    ```

### Get All Users

- **Endpoint**: `GET /users`
- **Description**: Retrieves a list of all users.
- **Example** 
    ```bash
    curl -XGET --insecure "http://localhost:5000/users"
    ```


### Get User by ID

- **Endpoint**: `GET /users/<id>`
- **Description**: Retrieves a user by their unique ID.
- **Example** 
    ```bash
    curl -XGET --insecure "http://localhost:5000/users/6706182ab8095c5d36f422f3"
    ```

### Update User by ID

- **Endpoint**: `PUT /users/<id>`
- **Description**: Updates an existing user by their unique ID.
- **Example** 
    ```bash
     curl -XPUT --insecure "http://localhost:5000/users/670617e4b8095c5d36f422f2" -H 'Content-Type: application/json' -d '{
        "username": "test",
            "password": "password123"
        }'
    ```

### Delete User by ID

- **Endpoint**: `DELETE /users/<id>`
- **Description**: Deletes a user by their unique ID.
- **Example** 
    ```bash
    curl -XDELETE --insecure "http://localhost:5000/users/6706182ab8095c5d36f422f3"
    ```

### Login for User

- **Endpoint**: `POST /login`
- **Description**: Login API for User.
- **Example** 
    ```bash
     curl -XPOST --insecure "http://localhost:5000/login" -H 'Content-Type: application/json' -d '{
        "username": "vishal",
            "password": "password123"
        }'
    ```

### Login for Admin

- **Endpoint**: `POST /admin/login`
- **Description**: Login API for Admin User.
- **Example** 
    ```bash
     curl -XPOST --insecure "http://localhost:5000/admin/login" -H 'Content-Type: application/json' -d '{
            "username": "aad1",
                "password": "password123"
            }'
    ```

### Upload an Assignemnt

- **Endpoint**: `POST /upload`
- **Description**: Upload assignment.
- **Example** 
    ```bash
    curl -XPOST --insecure "http://localhost:5000/upload" -H 'Content-Type: application/json' -d '{
        "username" : "upload test", "task" :"Hello world", "admin":"ad1"
        }'
    ```

### Get assignmnet assigned to curent admin

- **Endpoint**: `GET /assigments`
- **Description**: Get assigments.
- **Request Parameters**: `username` : Name of the admin

- **Example** 
    ```bash
    curl -XGET --insecure "http://localhost:5000/assignments?username=admin1"
    ```

### Accept the assignment

- **Endpoint**: `POST /assignments/<id>/accept`
- **Description**: Accept the assignment.

- **Example** 
    ```bash
    curl -XPOST --insecure "http://localhost:5000/assignments/6706182ab8095c5d36f422f3/accept"
    ```

### Reject the assignment

- **Endpoint**: `POST /assignments/<id>/reject`
- **Description**: Accept the assignment.

- **Example** 
    ```bash
    curl -XPOST --insecure "http://localhost:5000/assignments/6706182ab8095c5d36f422f3/reject"
    ```