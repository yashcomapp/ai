#!/usr/bin/env bash
set -e

echo "=================================================="
echo "🚀 DEPLOYING LOS TO GOOGLE CLOUD RUN"
echo "=================================================="

# Pull latest code from GitHub
git pull

# Deploy via official Cloud Run source builder (guaranteed permissions & network)
gcloud run deploy los-next \
  --source . \
  --region asia-south1 \
  --allow-unauthenticated

echo "✅ Cloud Run deployment completed successfully!"
