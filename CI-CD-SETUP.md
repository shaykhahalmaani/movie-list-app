# CI/CD Setup Guide

This guide explains how to set up the Continuous Integration and Continuous Deployment pipelines for the Movie List Application.

## Overview

The project includes four GitHub Actions workflows:
- `backend-ci.yml` - Backend testing and linting
- `backend-cd.yml` - Backend deployment to EKS
- `frontend-ci.yml` - Frontend testing and building
- `frontend-cd.yml` - Frontend deployment to EKS

## Prerequisites

### AWS Setup
1. **EKS Cluster**: Create an EKS cluster named `movie-app-cluster`
2. **ECR Repositories**: Create repositories for `backend` and `frontend`
3. **IAM User**: Create an IAM user with necessary permissions

### Required IAM Permissions
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ecr:GetAuthorizationToken",
                "ecr:BatchCheckLayerAvailability",
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchGetImage",
                "ecr:InitiateLayerUpload",
                "ecr:UploadLayerPart",
                "ecr:CompleteLayerUpload",
                "ecr:PutImage",
                "eks:DescribeCluster",
                "eks:ListClusters"
            ],
            "Resource": "*"
        }
    ]
}
```

## GitHub Secrets Setup

Add these secrets to your GitHub repository:

1. Go to your repository → Settings → Secrets and variables → Actions
2. Add the following secrets:

### Required Secrets
- `AWS_ACCESS_KEY_ID`: Your AWS access key
- `AWS_SECRET_ACCESS_KEY`: Your AWS secret key

## Workflow Triggers

### CI Workflows
- Triggered on push to `main` or `develop` branches
- Triggered on pull requests to `main` branch
- Only runs when files in respective directories change

### CD Workflows
- Triggered on push to `main` branch
- Only runs when files in respective directories change

## Workflow Details

### Backend CI
- Sets up Python 3.10
- Installs dependencies with pipenv
- Runs tests with pytest
- Runs linting with flake8

### Backend CD
- Builds Docker image
- Pushes to ECR
- Updates EKS deployment
- Waits for rollout completion

### Frontend CI
- Sets up Node.js 18
- Installs dependencies with npm
- Runs tests with Jest
- Runs linting with ESLint
- Builds the application

### Frontend CD
- Builds Docker image
- Pushes to ECR
- Updates EKS deployment
- Waits for rollout completion

## Customization

### Environment Variables
Update the following in the CD workflows:
- `aws-region`: Change to your preferred region
- `movie-app-cluster`: Change to your EKS cluster name
- ECR repository names

### Build Arguments
Add build arguments to Dockerfiles if needed:
```yaml
- name: Build image
  run: |
    docker build --build-arg NODE_ENV=production -t $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG ./frontend
```

## Monitoring

### GitHub Actions
- View workflow runs in the Actions tab
- Check logs for any failures
- Monitor deployment status

### EKS
```bash
# Check deployment status
kubectl get deployments

# Check pod status
kubectl get pods

# View logs
kubectl logs -f deployment/backend-deployment
kubectl logs -f deployment/frontend-deployment
```

## Troubleshooting

### Common Issues

1. **ECR Push Fails**:
   - Check AWS credentials
   - Verify ECR repository exists
   - Check IAM permissions

2. **EKS Deployment Fails**:
   - Verify cluster name
   - Check kubectl configuration
   - Verify image exists in ECR

3. **Tests Fail**:
   - Check test files
   - Verify dependencies
   - Review test logs

### Debug Commands
```bash
# Check ECR images
aws ecr list-images --repository-name backend

# Check EKS cluster
aws eks describe-cluster --name movie-app-cluster

# Check deployment
kubectl describe deployment backend-deployment
```

## Best Practices

1. **Branch Protection**: Enable branch protection rules
2. **Required Checks**: Require CI checks to pass before merging
3. **Review Process**: Require pull request reviews
4. **Security**: Regularly rotate AWS credentials
5. **Monitoring**: Set up alerts for failed deployments
