#!/usr/bin/env bash
set -e

echo "=================================================="
echo "⚡ FAST CLOUD RUN DEPLOYMENT (CACHED DOCKER PIPELINE)"
echo "=================================================="

# Pull latest code from GitHub
git pull

IMAGE_URI="asia-south1-docker.pkg.dev/ai-yashcom/cloud-run-source-deploy/los-next:latest"

echo "📦 Building container using persistent Cloud Shell Docker layer cache..."
docker build -t "$IMAGE_URI" .

echo "📤 Pushing optimized image to Google Artifact Registry..."
docker push "$IMAGE_URI"

echo "🚀 Deploying pre-built container to Cloud Run..."
gcloud run deploy los-next \
  --image "$IMAGE_URI" \
  --region asia-south1 \
  --allow-unauthenticated

echo "✅ Deployment finished successfully!"
