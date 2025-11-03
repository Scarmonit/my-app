#!/usr/bin/env python3
"""
Simple test script to verify the Cooking AI Agent setup.
"""

import os
import sys

def test_imports():
    """Test that all required packages are installed."""
    print("Testing imports...")
    try:
        from azure.ai.inference import ChatCompletionsClient
        from azure.ai.inference.models import SystemMessage, UserMessage
        from azure.core.credentials import AzureKeyCredential
        print("✅ All required packages are installed")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def test_token():
    """Test that GitHub token is available."""
    print("\nTesting GitHub token...")
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        # Only show first and last 4 characters for security
        masked_token = f"{token[:4]}...{token[-4:]}" if len(token) > 8 else "****"
        print(f"✅ GitHub token found: {masked_token}")
        return True
    else:
        print("❌ GitHub token not found")
        print("Please set GITHUB_TOKEN environment variable")
        return False

def test_agent_initialization():
    """Test that the CookingAIAgent can be initialized."""
    print("\nTesting agent initialization...")
    try:
        # Import after we know packages are installed
        from cooking_agent import CookingAIAgent
        agent = CookingAIAgent()
        print("✅ CookingAIAgent initialized successfully")
        return True
    except Exception as e:
        print(f"❌ Failed to initialize agent: {e}")
        return False

def main():
    """Run all tests."""
    print("="*60)
    print("Cooking AI Agent - Setup Test")
    print("="*60)
    print()
    
    tests = [
        test_imports,
        test_token,
        test_agent_initialization
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("\n" + "="*60)
    if all(results):
        print("✅ All tests passed! You're ready to use the Cooking AI Agent.")
        print("\nRun the application with:")
        print("  python cooking_agent.py")
    else:
        print("❌ Some tests failed. Please fix the issues above.")
        sys.exit(1)
    print("="*60)

if __name__ == "__main__":
    main()
