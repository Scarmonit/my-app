#!/bin/bash

# Deploy-all script - wrapper for consistent deployments using Task
# This script provides a unified interface for deploying all environments

set -e

echo "==============================================="
echo "  Multi-Environment Deployment Script"
echo "==============================================="
echo ""

# Check if Task is installed
if ! command -v task &> /dev/null; then
    echo "Error: Task (go-task) is not installed."
    echo "Please install Task from: https://taskfile.dev/installation/"
    exit 1
fi

# Function to display usage
usage() {
    echo "Usage: $0 [ENVIRONMENT]"
    echo ""
    echo "Environments:"
    echo "  dev       Deploy to development environment"
    echo "  prod      Deploy to production environment"
    echo "  all       Deploy to all environments (dev then prod)"
    echo ""
    echo "Example:"
    echo "  $0 dev"
    echo "  $0 prod"
    echo "  $0 all"
    exit 1
}

# Check for arguments
if [ $# -eq 0 ]; then
    echo "Error: No environment specified."
    echo ""
    usage
fi

ENVIRONMENT=$1

# Deploy based on environment
case $ENVIRONMENT in
    dev)
        echo "Deploying to DEVELOPMENT environment..."
        task deploy:dev
        echo ""
        echo "✓ Development deployment complete!"
        ;;
    prod)
        echo "Deploying to PRODUCTION environment..."
        echo "⚠️  Warning: This will deploy to production!"
        read -p "Continue? (y/N): " -n 1 -r
        echo ""
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            task deploy:prod
            echo ""
            echo "✓ Production deployment complete!"
        else
            echo "Production deployment cancelled."
            exit 0
        fi
        ;;
    all)
        echo "Deploying to ALL environments..."
        echo ""
        echo "Step 1: Development Environment"
        task deploy:dev
        echo ""
        echo "✓ Development deployment complete!"
        echo ""
        echo "Step 2: Production Environment"
        echo "⚠️  Warning: This will deploy to production!"
        read -p "Continue with production deployment? (y/N): " -n 1 -r
        echo ""
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            task deploy:prod
            echo ""
            echo "✓ Production deployment complete!"
            echo ""
            echo "✓ All environments deployed successfully!"
        else
            echo "Production deployment skipped."
            echo "✓ Development deployment complete, production skipped."
        fi
        ;;
    *)
        echo "Error: Unknown environment '$ENVIRONMENT'"
        echo ""
        usage
        ;;
esac

echo ""
echo "==============================================="
echo "  Deployment Complete"
echo "==============================================="
