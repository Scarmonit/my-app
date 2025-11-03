# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)

## Automation & Development Tools

This project includes comprehensive automation scaffolding for streamlined development, testing, and deployment.

### Task Automation

The project uses [Task](https://taskfile.dev) for task automation. Install Task following the [official installation guide](https://taskfile.dev/installation/).

#### Available Tasks

View all available tasks:
```bash
task --list
```

Common tasks:
```bash
task install           # Install project dependencies
task dev              # Start development server
task dev:setup        # Setup development environment
task lint             # Run linter
task lint:fix         # Run linter with auto-fix
task test             # Run tests
task test:coverage    # Run tests with coverage
task build            # Build for production
task ci               # Run full CI pipeline locally
```

### Docker Support

The project includes Docker configurations for both development and production environments.

#### Development Environment

```bash
task docker:build:dev    # Build development Docker image
task docker:up:dev       # Start development containers
task docker:down:dev     # Stop development containers
```

Or using docker-compose directly:
```bash
docker-compose -f docker-compose.dev.yml up
```

#### Production Environment

```bash
task docker:build:prod   # Build production Docker image
task docker:up:prod      # Start production containers
task docker:down:prod    # Stop production containers
```

Or using docker-compose directly:
```bash
docker-compose -f docker-compose.prod.yml up
```

### Deployment

Deploy to specific environments using the deployment wrapper script:

```bash
./deploy-all.sh dev      # Deploy to development
./deploy-all.sh prod     # Deploy to production (with confirmation)
./deploy-all.sh all      # Deploy to all environments
```

Or using Task:
```bash
task deploy:dev          # Deploy to development
task deploy:prod         # Deploy to production
task deploy:all          # Deploy all environments
```

### CI/CD Pipeline

The project includes a comprehensive GitHub Actions CI/CD pipeline that:

1. **Lint**: Runs ESLint on all code changes
2. **Test & Build**: Runs tests with coverage and builds the application on Node.js 18.x and 20.x
3. **Docker Build**: Builds both development and production Docker images
4. **Deploy**: Automatically deploys to development and production environments on main branch

The pipeline runs on every push to main and on all pull requests.
