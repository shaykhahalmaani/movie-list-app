# Movie List Application

A full-stack movie list application built with Flask backend and React frontend, deployed on AWS EKS with CI/CD pipelines.

## Features

- **Backend API**: Flask-based REST API serving movie data
- **Frontend**: React application with movie list and details view
- **Containerization**: Docker containers for both services
- **Orchestration**: Kubernetes deployment on AWS EKS
- **CI/CD**: Automated testing and deployment with GitHub Actions

## Project Structure

```
├── backend/                 # Flask API
│   ├── movies/             # Movie API modules
│   ├── k8s/               # Kubernetes manifests
│   ├── Dockerfile         # Backend container
│   └── Pipfile           # Python dependencies
├── frontend/              # React application
│   ├── src/              # React source code
│   ├── k8s/              # Kubernetes manifests
│   ├── Dockerfile        # Frontend container
│   └── package.json      # Node.js dependencies
└── .github/workflows/    # CI/CD pipelines
```

## Quick Start

### Prerequisites

- Docker
- Kubernetes cluster (EKS recommended)
- AWS CLI configured
- kubectl configured

### Local Development

1. **Backend Setup**:
   ```bash
   cd backend
   pipenv install
   pipenv run python app.py
   ```

2. **Frontend Setup**:
   ```bash
   cd frontend
   npm install
   npm start
   ```

### Docker Build

```bash
# Build backend
docker build -t movie-backend ./backend

# Build frontend
docker build -t movie-frontend ./frontend
```

### Kubernetes Deployment

```bash
# Deploy backend
kubectl apply -k backend/k8s/

# Deploy frontend
kubectl apply -k frontend/k8s/
```

## API Endpoints

- `GET /movies` - Get all movies
- `GET /movies/{id}` - Get movie details by ID

## Environment Variables

- `REACT_APP_MOVIE_API_URL` - Backend API URL for frontend

## CI/CD

The project includes GitHub Actions workflows for:
- Backend CI/CD
- Frontend CI/CD
- Automated testing and deployment to EKS

## Screenshots

See the `ScreenShots/` directory for deployment and application screenshots.

## License

This project is licensed under the MIT License.
