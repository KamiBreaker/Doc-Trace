# Deployment Guide for DocuTrace AI

This project is set up to run with Docker and Docker Compose.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed on your machine.
- [Docker Compose](https://docs.docker.com/compose/install/) (usually included with Docker Desktop).

## Running Locally

1.  **Build and Start the Services:**

    Run the following command in the root directory (where `docker-compose.yml` is located):

    ```bash
    docker-compose up --build
    ```

    This will:
    - Build the backend Docker image.
    - Start a PostgreSQL database container.
    - Run the database schema migration script (`backend/sql/schema.sql`).
    - Start the FastAPI backend server.

2.  **Access the Application:**

    The backend API will be available at: http://localhost:8000
    API Documentation (Swagger UI): http://localhost:8000/docs

3.  **Stopping the Services:**

    To stop the running containers, press `Ctrl+C` or run:

    ```bash
    docker-compose down
    ```

    To stop and also remove the database volume (reset data), run:

    ```bash
    docker-compose down -v
    ```

## Cloud Deployment

This setup is compatible with cloud providers that support Docker or Docker Compose (e.g., AWS, Azure, Google Cloud, DigitalOcean).

For platforms like **Render** or **Railway**:
1.  Connect your repository.
2.  Set the build command to install dependencies.
3.  Set the start command to `uvicorn app.main:app --host 0.0.0.0 --port $PORT`.
4.  Ensure you provision a PostgreSQL database and provide the `DATABASE_URL` environment variable.
