# 🍳 Cooking AI Agent

An interactive console-based AI cooking assistant powered by GitHub Models. This application leverages AI language models to provide recipe search, ingredient extraction, and cooking tips.

## Features

- **🔍 Recipe Search**: Find recipes based on ingredients, cuisine type, and dietary restrictions
- **📋 Ingredient Extraction**: Automatically extract ingredients and quantities from recipe texts
- **💡 Cooking Tips**: Get expert cooking tips and techniques for any dish
- **🤖 AI-Powered**: Uses GitHub Models API with GPT-4 for intelligent responses
- **📱 Interactive Console**: User-friendly command-line interface

## Prerequisites

- Python 3.7 or higher
- GitHub account with access to GitHub Models
- GitHub Personal Access Token

## Setup

### Quick Start (Recommended)

Run the automated setup script:

```bash
cd cooking-ai-agent
./setup.sh
```

This will install dependencies and guide you through creating your `.env` file.

### Manual Setup

### 1. Get Your GitHub Token

1. Go to [GitHub Settings > Personal Access Tokens](https://github.com/settings/tokens)
2. Click "Generate new token (classic)"
3. Give it a descriptive name (e.g., "Cooking AI Agent")
4. Select the `read:user` scope (required for GitHub Models access)
5. Click "Generate token"
6. **Important**: Copy the token immediately (you won't be able to see it again)

### 2. Install Dependencies

```bash
# Navigate to the cooking-ai-agent directory
cd cooking-ai-agent

# Install required Python packages
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file or set the environment variable:

**Option A: Using .env file**
```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your token
# GITHUB_TOKEN=your_actual_token_here
```

**Option B: Export environment variable**
```bash
export GITHUB_TOKEN=your_actual_token_here
```

## Usage

Run the application:

```bash
python cooking_agent.py
```

Or make it executable and run directly:

```bash
chmod +x cooking_agent.py
./cooking_agent.py
```

### Interactive Menu

Once started, you'll see a menu with the following options:

1. **Search for recipes** - Find recipes based on your preferences
2. **Extract ingredients from recipe** - Parse recipe text to get ingredients list
3. **Get cooking tips** - Receive expert cooking advice
4. **Exit** - Quit the application

### Example Usage

#### Recipe Search
```
What would you like to cook?: pasta carbonara
Cuisine type (press Enter to skip): Italian
Dietary restrictions (comma-separated, press Enter to skip): 

🤖 Searching for recipes...
```

#### Ingredient Extraction
```
Paste or type your recipe (press Enter twice when done):
Classic Spaghetti Carbonara
Ingredients: 400g spaghetti, 200g pancetta, 4 eggs, ...

🤖 Extracting ingredients...
```

#### Cooking Tips
```
What dish do you need tips for?: risotto

🤖 Getting cooking tips...
```

## Configuration

### Model Selection

By default, the application uses `gpt-4o`. You can specify a different model:

```python
agent = CookingAIAgent(model="gpt-4o-mini")
```

Available models:
- `gpt-4o` (default, most capable)
- `gpt-4o-mini` (faster, more cost-effective)
- `gpt-4`
- `gpt-35-turbo`

### Programmatic Usage

You can also use the `CookingAIAgent` class programmatically:

```python
from cooking_agent import CookingAIAgent

# Initialize the agent
agent = CookingAIAgent()

# Search for recipes
result = agent.search_recipes(
    query="chocolate cake",
    cuisine="French",
    dietary_restrictions=["vegetarian"]
)

if result["success"]:
    print(result["recipe"])

# Extract ingredients
result = agent.extract_ingredients(
    "Mix flour, sugar, eggs, and butter. Bake at 350°F for 30 minutes."
)

if result["success"]:
    print(result["ingredients"])

# Get cooking tips
result = agent.get_cooking_tips("risotto")

if result["success"]:
    print(result["tips"])
```

## Architecture

The application consists of a single Python module with the following components:

- **CookingAIAgent**: Main class that handles AI model interactions
  - `search_recipes()`: Recipe search functionality
  - `extract_ingredients()`: Ingredient extraction
  - `get_cooking_tips()`: Cooking tips and techniques

- **Interactive Interface**: Console-based UI with menu system
  - Input validation
  - Error handling
  - Formatted output

## Error Handling

The application includes comprehensive error handling:

- Missing or invalid GitHub token
- API connection errors
- Empty or invalid user inputs
- Model API errors

## Best Practices

1. **Keep your token secure**: Never commit your `.env` file or share your token
2. **Rate limits**: Be mindful of API rate limits when making multiple requests
3. **Token scopes**: Only grant necessary scopes to your GitHub token
4. **Model selection**: Use `gpt-4o-mini` for faster responses and lower costs during development

## Troubleshooting

### "GitHub token not found" error
- Ensure you've set the `GITHUB_TOKEN` environment variable
- Check that your token has the correct scopes

### Import errors
- Run `pip install -r requirements.txt` to install dependencies
- Ensure you're using Python 3.7+

### API errors
- Verify your GitHub token is valid and hasn't expired
- Check your internet connection
- Ensure you have access to GitHub Models

## Contributing

This is a sample application demonstrating GitHub Models integration. Feel free to extend it with:

- Recipe saving and bookmarking
- Meal planning features
- Nutrition information
- Shopping list generation
- Recipe scaling

## License

This project is provided as-is for educational and demonstration purposes.

## Acknowledgments

- Powered by [GitHub Models](https://github.com/marketplace/models)
- Uses Azure AI Inference SDK
- Built with Python 3
