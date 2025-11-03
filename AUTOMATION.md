# Automation Setup Guide

This document provides instructions for using the automation tools configured in this repository.

## Prerequisites

- **Node.js** 18.x or 20.x
- **npm** (comes with Node.js)
- **Git**
- **Task** (optional, for Taskfile automation) - [Installation Guide](https://taskfile.dev/installation/)
- **Docker** (optional, for containerized development) - [Installation Guide](https://docs.docker.com/get-docker/)

## Quick Start

### Using npm scripts (Standard)

```bash
# Install dependencies
npm install

# Start development server
npm start

# Run tests
npm test

# Build for production
npm run build
```

### Using Task (Recommended for automation)

If you have [Task](https://taskfile.dev/) installed:

```bash
# View all available tasks
task

# Setup development environment
task setup

# Start development server
task dev

# Run tests with coverage
task test:coverage

# Build production bundle
task build

# Run CI pipeline locally
task ci
```

## Environment Configuration

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Update `.env` with your configuration values.

## Docker Development

### Development Environment

```bash
# Build and start development containers
task docker:up:dev
# or
docker-compose -f docker-compose.dev.yml up

# Stop containers
task docker:down:dev
```

### Production Environment

```bash
# Build and start production containers
task docker:up:prod
# or
docker-compose -f docker-compose.prod.yml up -d

# Stop containers
task docker:down:prod
```

## Deployment

### Automated Deployment

```bash
# Deploy to production
task deploy
# or
./deploy-all.sh production

# Deploy to staging
./deploy-all.sh staging
```

### Manual Deployment

1. Run tests:
   ```bash
   npm test -- --coverage --watchAll=false
   ```

2. Build the application:
   ```bash
   npm run build
   ```

3. Deploy the `build/` directory to your hosting service.

### AWS S3 Deployment

To enable AWS S3 deployment, set the following environment variables:

```bash
export AWS_S3_BUCKET=your-bucket-name
export AWS_CLOUDFRONT_DISTRIBUTION_ID=your-distribution-id (optional)
```

Then run:
```bash
./deploy-all.sh production
```

## Continue IDE Setup

This repository includes configuration for the [Continue](https://continue.dev/) VS Code extension.

### Setup

1. Install the Continue extension in VS Code
2. Update `.continue/config.json` with your API keys:
   - OpenAI API Key (for GPT models)
   - Anthropic API Key (for Claude models)
   - Mistral API Key (for Codestral autocomplete)

### Features

- **Code Completion**: Tab autocomplete powered by Codestral
- **Custom Commands**:
  - `/test` - Generate comprehensive tests
  - `/review` - Code review assistance
  - `/docs` - Generate documentation
  - `/refactor` - Refactoring suggestions
- **Context Providers**: Code, docs, diff, terminal, problems, folder, codebase

## CI/CD Pipeline

The project uses GitHub Actions for continuous integration:

- **Trigger**: Push to `main` or Pull Requests
- **Node Versions**: 18.x, 20.x
- **Steps**:
  1. Install dependencies
  2. Run tests with coverage
  3. Build production bundle
  4. Upload coverage reports

## Available Task Commands

| Command | Description |
|---------|-------------|
| `task` | Show all available tasks |
| `task setup` | Setup development environment |
| `task dev` | Run development server |
| `task build` | Build production bundle |
| `task test` | Run tests |
| `task test:coverage` | Run tests with coverage |
| `task lint` | Lint code |
| `task lint:fix` | Lint and fix code |
| `task clean` | Clean build artifacts |
| `task docker:build:dev` | Build development Docker image |
| `task docker:up:dev` | Start development containers |
| `task docker:down:dev` | Stop development containers |
| `task docker:build:prod` | Build production Docker image |
| `task docker:up:prod` | Start production containers |
| `task docker:down:prod` | Stop production containers |
| `task deploy` | Deploy application |
| `task ci` | Run CI pipeline locally |

## Troubleshooting

### Task not found

Install Task following the [official installation guide](https://taskfile.dev/installation/).

### Docker issues

- Ensure Docker is running: `docker ps`
- Check Docker Compose version: `docker-compose --version`

### npm install fails

- Clear npm cache: `npm cache clean --force`
- Delete `node_modules` and `package-lock.json`, then reinstall

### Build fails

- Check Node.js version: `node --version` (should be 18.x or 20.x)
- Ensure all dependencies are installed: `npm install`

## Additional Resources

- [Create React App Documentation](https://create-react-app.dev/)
- [Task Documentation](https://taskfile.dev/)
- [Docker Documentation](https://docs.docker.com/)
- [Continue Documentation](https://continue.dev/docs)
