
# FastAPI + MongoDB Backend with Docker

This project implements a backend API using **FastAPI** and **MongoDB**, all containerized using **Docker**. The application includes the following features:
- CRUD operations for a movie database.
- MongoDB as the database for storing movie data.
- Docker for containerizing both FastAPI and MongoDB.
- Docker Compose for managing multiple services.

## Table of Contents
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Using Docker](#using-docker)
- [Technologies](#technologies)

---

## Project Structure

```bash
.
├── backend
│   ├── __pycache__
│   ├── create_database.py
│   ├── database.py
│   ├── Dockerfile
│   ├── main.py
│   ├── models.py
│   ├── requirements.txt
├── venv
├── docker-compose.yml
└── README.md
```

- `backend/`: Contains all the backend Python code, including the FastAPI implementation, database connection, and models.
- `Dockerfile`: Docker configuration for the FastAPI backend.
- `docker-compose.yml`: Configuration file for Docker Compose, managing both FastAPI and MongoDB services.
- `requirements.txt`: Python dependencies needed for the backend.

---

## Installation

### Prerequisites:
- **Docker** and **Docker Compose** installed on your system.
- **Python** 3.9+ installed locally.

### Clone the repository:
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### Set up the virtual environment:
You can skip this step if you are using Docker. If you'd like to run the project locally without Docker, set up the environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r backend/requirements.txt
```

---

## Running the Application

You can run the application using Docker Compose or locally.

### Using Docker Compose:

1. **Build and run the containers**:
   ```bash
   docker-compose up --build
   ```

   This will start:
   - The **FastAPI** backend at `http://localhost:8000`.
   - The **MongoDB** service at `localhost:27017`.

2. **Stop the services**:
   ```bash
   docker-compose down
   ```

### Running Locally:

1. **Start MongoDB** on your local machine (you can use **MongoDB Compass** for managing the database).
2. **Run the FastAPI server**:
   ```bash
   uvicorn backend.main:app --reload
   ```

---

## API Endpoints

Here are the main API endpoints for interacting with the movie database:

### Movies Endpoints:

- **GET** `/movies/`: Retrieve all movies.
- **POST** `/movie/`: Add a new movie.
- **PUT** `/movie/{title}`: Update an existing movie by title.
- **DELETE** `/movie/{title}`: Delete a movie by title.

### Example cURL for adding a movie:
```bash
curl -X 'POST'   'http://localhost:8000/movie/'   -H 'Content-Type: application/json'   -d '{
  "title": "Inception",
  "director": "Christopher Nolan",
  "year": 2010
}'
```

---

## Using Docker

### Dockerfile

The **Dockerfile** in the `backend/` directory is used to build the FastAPI application container. The Dockerfile:
- Uses a **Python 3.9 slim** image.
- Installs dependencies from `requirements.txt`.
- Exposes the FastAPI service on port 8000.

### docker-compose.yml

The **docker-compose.yml** file orchestrates both **FastAPI** and **MongoDB** services.

Here is an overview of the `docker-compose.yml`:
```yaml
version: "3.8"

services:
  backend:
    build: ./backend
    container_name: fastapi-backend
    ports:
      - "8000:8000"
    volumes:
      - ./backend:/app
    depends_on:
      - mongo
    environment:
      - MONGO_URL=mongodb://mongo:27017
    command: ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

  mongo:
    image: mongo:5.0
    container_name: mongodb
    ports:
      - "27017:27017"
    volumes:
      - mongo-data:/data/db

volumes:
  mongo-data:
```

This configuration ensures both the **backend** and **MongoDB** services run inside their own containers, with MongoDB exposed on port 27017 and the FastAPI backend on port 8000.

---

## Technologies

- **FastAPI**: High-performance API framework.
- **MongoDB**: NoSQL database for storing movie data.
- **Docker**: Containerization of the application.
- **Docker Compose**: Orchestrates multiple Docker containers.
- **Python 3.9**: Backend development.

---

## Next Steps

- Add authentication and authorization.
- Create advanced filters for querying movies.
- Deploy the application to a cloud provider (e.g., AWS, Heroku).

---

Feel free to modify the instructions based on the specific requirements of your project, or include additional sections as your project evolves!
