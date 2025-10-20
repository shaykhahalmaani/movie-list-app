# Service URLs

This document contains the URLs for accessing the deployed services.

## Local Development

- **Backend API**: http://localhost:5000
- **Frontend App**: http://localhost:3000

## Production (EKS)

### Backend Service
- **LoadBalancer URL**: `http://<backend-lb-url>`
- **API Endpoints**:
  - `GET /movies` - List all movies
  - `GET /movies/{id}` - Get movie details

### Frontend Service
- **LoadBalancer URL**: `http://<frontend-lb-url>`
- **Application**: Movie List Interface

## Getting Service URLs

To get the actual LoadBalancer URLs:

```bash
# Get all services
kubectl get services

# Get specific service URLs
kubectl get service backend-service -o jsonpath='{.status.loadBalancer.ingress[0].hostname}'
kubectl get service frontend-service -o jsonpath='{.status.loadBalancer.ingress[0].hostname}'
```

## Example URLs

After deployment, your URLs might look like:
- Backend: `http://a1234567890abcdef-1234567890.us-west-2.elb.amazonaws.com`
- Frontend: `http://b0987654321fedcba-0987654321.us-west-2.elb.amazonaws.com`

## Testing the Application

1. **Test Backend API**:
   ```bash
   curl http://<backend-lb-url>/movies
   ```

2. **Test Frontend**:
   - Open `http://<frontend-lb-url>` in your browser
   - Click on any movie to see details

## Environment Variables

Make sure the frontend has the correct backend URL:
```bash
kubectl set env deployment/frontend-deployment REACT_APP_MOVIE_API_URL=http://<backend-lb-url>
```
