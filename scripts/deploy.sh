#!/usr/bin/env bash
set -e

echo "=================================================="
echo "🚀 DEPLOYING LOS TO GOOGLE CLOUD RUN"
echo "=================================================="

# Pull latest code from GitHub
git pull

# Deploy via Cloud Build pipeline (enforces default free-tier machine, layer cache, & Artifact Registry 0.5 GB pruning)
gcloud builds submit --config=cloudbuild.yaml .

echo "✅ Cloud Run deployment completed successfully!"
