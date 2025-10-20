# Setup Guide

This guide will help you set up the Movie List Application from scratch.

## Prerequisites

### Required Software
- Docker
- kubectl
- AWS CLI
- Node.js 18+
- Python 3.10+
- pipenv

### AWS Account Setup
1. Create an AWS account
2. Configure AWS CLI with your credentials
3. Create an EKS cluster
4. Set up ECR repositories for backend and frontend

## Step 1: Clone and Setup

```bash
git clone <your-repo-url>
cd Project-4Sh
```

## Step 2: Backend Setup

```bash
cd backend

# Install dependencies
pipenv install

# Run tests
pipenv run pytest

# Start development server
pipenv run python app.py
```

The backend will be available at `http://localhost:5000`

## Step 3: Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Set environment variable
export REACT_APP_MOVIE_API_URL=http://localhost:5000

# Start development server
npm start
```

The frontend will be available at `http://localhost:3000`

## Step 4: Docker Build

```bash
# Build backend image
docker build -t movie-backend ./backend

# Build frontend image
docker build -t movie-frontend ./frontend
```

## Step 5: Kubernetes Deployment

### Prerequisites
- EKS cluster running
- kubectl configured to access your cluster

```bash
# Deploy backend
kubectl apply -k backend/k8s/

# Deploy frontend
kubectl apply -k frontend/k8s/

# Check deployment status
kubectl get pods
kubectl get services
```

## Step 6: CI/CD Setup

### GitHub Secrets
Add these secrets to your GitHub repository:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`

### ECR Repositories
Create ECR repositories:
- `backend`
- `frontend`

## Step 7: Verification

1. Check that pods are running:
   ```bash
   kubectl get pods
   ```

2. Get service URLs:
   ```bash
   kubectl get services
   ```

3. Test the application:
   - Backend: `http://<backend-lb-url>/movies`
   - Frontend: `http://<frontend-lb-url>`

## Troubleshooting

### Common Issues

1. **Pods not starting**: Check logs with `kubectl logs <pod-name>`
2. **Services not accessible**: Verify LoadBalancer status
3. **API connection issues**: Check environment variables and network policies

### Useful Commands

```bash
# View pod logs
kubectl logs -f deployment/backend-deployment
kubectl logs -f deployment/frontend-deployment

# Scale deployments
kubectl scale deployment backend-deployment --replicas=3

# Update image
kubectl set image deployment/backend-deployment backend=new-image:tag
```

## Next Steps

- Set up monitoring and logging
- Configure auto-scaling
- Add security policies
- Set up backup strategies
