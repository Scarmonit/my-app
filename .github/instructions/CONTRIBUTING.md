# Contributing to my-app

Thank you for your interest in contributing to my-app! This guide will help you get started.

## 🚀 Quick Start

### Prerequisites
- Node.js 18.x or 20.x
- npm (comes with Node.js)
- Git

### Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Scarmonit/my-app.git
   cd my-app
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Run the development server**
   ```bash
   npm start
   ```
   The app will open at [http://localhost:3000](http://localhost:3000)

4. **Run tests**
   ```bash
   npm test
   ```

5. **Build for production**
   ```bash
   npm run build
   ```

## 📋 Development Workflow

### 1. Create a Feature Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 2. Make Your Changes
- Write clean, readable code
- Follow existing code style and patterns
- Add tests for new features
- Update documentation as needed

### 3. Test Your Changes
```bash
# Run all tests
npm test

# Run tests with coverage
npm test -- --coverage --watchAll=false

# Build to ensure no build errors
npm run build
```

### 4. Commit Your Changes
Use clear, descriptive commit messages:
```bash
git add .
git commit -m "feat: add new feature description"
# or
git commit -m "fix: resolve specific bug"
```

**Commit Message Format:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc.)
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

### 5. Push and Create a Pull Request
```bash
git push origin feature/your-feature-name
```

Then open a Pull Request on GitHub with:
- Clear description of changes
- Reference to related issues (if any)
- Screenshots (for UI changes)

## 🧪 Testing Guidelines

- Write unit tests for all new functions/components
- Ensure all tests pass before submitting PR
- Maintain or improve code coverage
- Test edge cases and error scenarios

## 📝 Code Style

- Use meaningful variable and function names
- Keep functions small and focused
- Add comments for complex logic
- Follow React best practices
- Use ES6+ features appropriately

## 🐛 Reporting Bugs

When reporting bugs, please include:
- Clear description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Environment details (OS, browser, Node version)
- Screenshots or error messages

## 💡 Suggesting Features

Feature suggestions are welcome! Please:
- Check if the feature is already requested
- Clearly describe the use case
- Explain the expected behavior
- Consider implementation complexity

## 🔍 Code Review Process

1. All PRs require review before merging
2. Address review feedback promptly
3. Keep PRs focused and reasonably sized
4. Be respectful and constructive in discussions

## 🤝 Getting Help

- Open an issue for questions
- Check existing issues and documentation
- Review closed PRs for examples

## 📜 License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

**Thank you for contributing to my-app!** 🎉
