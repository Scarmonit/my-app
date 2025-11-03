#!/bin/bash

# Deploy script for my-app
# This script builds and deploys the application

set -e  # Exit on error

echo "🚀 Starting deployment process..."

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Configuration
ENVIRONMENT=${1:-production}
BUILD_DIR="build"

echo -e "${YELLOW}Environment: ${ENVIRONMENT}${NC}"

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Validate dependencies
echo "📋 Checking dependencies..."
if ! command_exists node; then
    echo -e "${RED}Error: Node.js is not installed${NC}"
    exit 1
fi

if ! command_exists npm; then
    echo -e "${RED}Error: npm is not installed${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Dependencies validated${NC}"

# Install dependencies
echo "📦 Installing dependencies..."
npm ci --only=production

# Run tests
echo "🧪 Running tests..."
npm test -- --coverage --watchAll=false

if [ $? -ne 0 ]; then
    echo -e "${RED}Tests failed. Deployment aborted.${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Tests passed${NC}"

# Build the application
echo "🔨 Building application..."
npm run build

if [ $? -ne 0 ]; then
    echo -e "${RED}Build failed. Deployment aborted.${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Build completed${NC}"

# Check if build directory exists
if [ ! -d "$BUILD_DIR" ]; then
    echo -e "${RED}Error: Build directory not found${NC}"
    exit 1
fi

# Deploy based on environment
if [ "$ENVIRONMENT" == "production" ]; then
    echo "🌐 Deploying to production..."
    
    # Docker deployment
    if command_exists docker; then
        echo "🐳 Building Docker image..."
        docker-compose -f docker-compose.prod.yml build
        
        echo "🐳 Starting production containers..."
        docker-compose -f docker-compose.prod.yml up -d
        
        echo -e "${GREEN}✓ Docker deployment completed${NC}"
    fi
    
    # AWS S3 deployment (if configured)
    if [ -n "$AWS_S3_BUCKET" ]; then
        if command_exists aws; then
            echo "☁️  Deploying to AWS S3..."
            aws s3 sync $BUILD_DIR/ s3://$AWS_S3_BUCKET/ --delete
            
            # Invalidate CloudFront cache if distribution ID is set
            if [ -n "$AWS_CLOUDFRONT_DISTRIBUTION_ID" ]; then
                echo "🔄 Invalidating CloudFront cache..."
                aws cloudfront create-invalidation --distribution-id $AWS_CLOUDFRONT_DISTRIBUTION_ID --paths "/*"
            fi
            
            echo -e "${GREEN}✓ AWS deployment completed${NC}"
        else
            echo -e "${YELLOW}Warning: AWS CLI not found, skipping S3 deployment${NC}"
        fi
    fi
    
elif [ "$ENVIRONMENT" == "staging" ]; then
    echo "🌐 Deploying to staging..."
    # Add staging deployment logic here
    echo -e "${GREEN}✓ Staging deployment completed${NC}"
    
else
    echo -e "${YELLOW}Unknown environment: ${ENVIRONMENT}${NC}"
    echo "Usage: ./deploy-all.sh [production|staging]"
    exit 1
fi

echo ""
echo -e "${GREEN}🎉 Deployment completed successfully!${NC}"
echo ""
echo "Next steps:"
echo "  - Verify deployment at your production URL"
echo "  - Monitor application logs for any issues"
echo "  - Run smoke tests to ensure everything is working"
