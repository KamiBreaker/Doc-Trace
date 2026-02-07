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

### Deploying to Render (Recommended)

This project includes a `render.yaml` (Blueprint) file that simplifies deployment on [Render](https://render.com/).

1.  **Push your code to GitHub/GitLab.**
2.  **Log in to Render** and go to the **Blueprints** section.
3.  **Connect your repository.**
4.  Render will automatically detect the `render.yaml` file and propose to create:
    -   A **PostgreSQL** database (Free Tier).
    -   A **Web Service** for the FastAPI backend (Free Tier).
5.  **Approve the Blueprint.** Render will provision the database, build the Docker container, and deploy your app.

#### Manual Deployment on Render (without Blueprint):
1.  **Create a New Web Service**: Connect your repo.
2.  **Runtime**: Select `Docker`.
3.  **Docker Context**: `backend`.
4.  **Dockerfile Path**: `backend/Dockerfile`.
5.  **Environment Variables**:
    -   `DATABASE_URL`: Copy the "Internal Database URL" from your Render PostgreSQL instance.
## Important Note on Resource Limits

The AI models used in this project (`SentenceTransformers` and `RoBERTa`) require a significant amount of RAM. 

- **Render Free Tier**: Provides 512MB RAM. This might be tight and could lead to `Out of Memory` (OOM) errors during the first download or during heavy usage.
- **Recommended**: If you experience crashes, consider upgrading to the **Starter** plan (2GB RAM) on Render for a more stable experience.


