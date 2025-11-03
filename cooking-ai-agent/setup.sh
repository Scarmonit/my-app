#!/bin/bash
# Quick start script for Cooking AI Agent

echo "======================================================================="
echo "🍳 Cooking AI Agent - Quick Start Setup"
echo "======================================================================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.7 or higher."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"
echo ""

# Check if pip is installed
if ! command -v pip3 &> /dev/null && ! command -v pip &> /dev/null; then
    echo "❌ pip is not installed. Please install pip."
    exit 1
fi

echo "✅ pip found"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt || pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo ""

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found"
    echo ""
    echo "To use the Cooking AI Agent, you need to create a .env file with your GitHub token."
    echo ""
    echo "Steps to get your GitHub token:"
    echo "1. Go to https://github.com/settings/tokens"
    echo "2. Click 'Generate new token (classic)'"
    echo "3. Give it a name (e.g., 'Cooking AI Agent')"
    echo "4. Select the 'read:user' scope"
    echo "5. Click 'Generate token'"
    echo "6. Copy the token"
    echo ""
    echo "Then create a .env file with:"
    echo "  GITHUB_TOKEN=your_token_here"
    echo ""
    read -p "Do you want to create a .env file now? (y/n) " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        read -p "Enter your GitHub token: " token
        echo "GITHUB_TOKEN=$token" > .env
        echo "✅ .env file created"
    else
        echo "⚠️  Please create a .env file manually before running the agent"
    fi
else
    echo "✅ .env file found"
fi

echo ""

# Run setup test
echo "🧪 Running setup test..."
python3 test_setup.py

if [ $? -eq 0 ]; then
    echo ""
    echo "======================================================================="
    echo "✅ Setup complete! You can now run the Cooking AI Agent:"
    echo ""
    echo "  python3 cooking_agent.py"
    echo ""
    echo "Or run the examples:"
    echo "  python3 examples.py"
    echo "======================================================================="
else
    echo ""
    echo "======================================================================="
    echo "⚠️  Setup test failed. Please check the errors above."
    echo "======================================================================="
fi
