# Social Networking API

This is a social networking application built with Django Rest Framework. It provides functionalities like user signup/login, searching users, sending/accepting/rejecting friend requests, and listing friends and pending requests.

## Installation Steps

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd socialnetwork
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply the migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser (optional but useful for admin access):
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Docker Setup

1. Build and run the Docker containers:
    ```sh
    docker-compose up --build
    ```

2. The application will be available at `http://localhost:8000`.

## API Endpoints

For detailed API documentation, import the provided Postman collection.

## Postman Collection

Import the following Postman collection to quickly test the API endpoints:
[Postman Collection Link](postman_collection.json)

1. http://localhost:8000:signup/
2. http://localhost:8000:login/
3. http://localhost:8000:search/
4. http://localhost:8000:friend-request/send/
5. http://localhost:8000:friend-request/respond/
6. http://localhost:8000:friends/
7. http://localhost:8000:friend-requests/
