#!/usr/bin/env python3
"""
Cooking AI Agent - An interactive console application for recipe search and ingredient extraction
using GitHub Models API.
"""

import os
import sys
from typing import List, Dict, Optional
import json

try:
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
except ImportError:
    print("Error: Required packages not installed.")
    print("Please run: pip install -r requirements.txt")
    sys.exit(1)


class CookingAIAgent:
    """AI-powered cooking assistant for recipe search and ingredient extraction."""
    
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4o"):
        """
        Initialize the Cooking AI Agent.
        
        Args:
            api_key: GitHub token for authentication. If None, reads from GITHUB_TOKEN env var.
            model: The model to use (default: gpt-4o)
        """
        self.api_key = api_key or os.environ.get("GITHUB_TOKEN")
        if not self.api_key:
            raise ValueError(
                "GitHub token not found. Please set GITHUB_TOKEN environment variable "
                "or pass api_key parameter."
            )
        
        self.model = model
        self.endpoint = "https://models.inference.ai.azure.com"
        self.client = ChatCompletionsClient(
            endpoint=self.endpoint,
            credential=AzureKeyCredential(self.api_key)
        )
        
    def search_recipes(self, query: str, cuisine: Optional[str] = None, 
                      dietary_restrictions: Optional[List[str]] = None) -> Dict:
        """
        Search for recipes based on query and optional filters.
        
        Args:
            query: The search query (e.g., "pasta", "chicken soup")
            cuisine: Optional cuisine type (e.g., "Italian", "Chinese")
            dietary_restrictions: Optional list of dietary restrictions (e.g., ["vegetarian", "gluten-free"])
            
        Returns:
            Dictionary containing recipe suggestions
        """
        system_prompt = """You are a helpful cooking assistant specializing in recipe recommendations.
        When asked about recipes, provide detailed, practical suggestions including:
        - Recipe name
        - Brief description
        - Main ingredients (list format)
        - Cooking time
        - Difficulty level
        - Step-by-step instructions
        
        Format your response as a well-structured, easy-to-read recipe."""
        
        user_prompt = f"Find me recipes for: {query}"
        
        if cuisine:
            user_prompt += f"\nCuisine: {cuisine}"
        
        if dietary_restrictions:
            user_prompt += f"\nDietary restrictions: {', '.join(dietary_restrictions)}"
        
        messages = [
            SystemMessage(content=system_prompt),
            UserMessage(content=user_prompt)
        ]
        
        try:
            response = self.client.complete(
                messages=messages,
                model=self.model,
                temperature=0.7,
                max_tokens=1500
            )
            
            return {
                "success": True,
                "query": query,
                "recipe": response.choices[0].message.content
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def extract_ingredients(self, recipe_text: str) -> Dict:
        """
        Extract ingredients from a recipe text or description.
        
        Args:
            recipe_text: Recipe description or full recipe text
            
        Returns:
            Dictionary containing extracted ingredients with quantities
        """
        system_prompt = """You are a helpful cooking assistant specializing in ingredient extraction.
        When given a recipe or meal description, extract all ingredients with their quantities.
        
        Format the output as a clear, organized list with:
        - Ingredient name
        - Quantity (with units)
        - Optional preparation notes (e.g., "diced", "chopped")
        
        Also provide:
        - Shopping list grouped by category (produce, dairy, meat, pantry, etc.)
        - Total estimated servings
        """
        
        user_prompt = f"Extract all ingredients from this recipe:\n\n{recipe_text}"
        
        messages = [
            SystemMessage(content=system_prompt),
            UserMessage(content=user_prompt)
        ]
        
        try:
            response = self.client.complete(
                messages=messages,
                model=self.model,
                temperature=0.3,
                max_tokens=1000
            )
            
            return {
                "success": True,
                "ingredients": response.choices[0].message.content
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def get_cooking_tips(self, dish: str) -> Dict:
        """
        Get cooking tips and techniques for a specific dish.
        
        Args:
            dish: Name of the dish
            
        Returns:
            Dictionary containing cooking tips
        """
        system_prompt = """You are an experienced chef providing cooking tips and techniques.
        Share professional insights, common mistakes to avoid, and pro tips."""
        
        user_prompt = f"Give me cooking tips and techniques for making: {dish}"
        
        messages = [
            SystemMessage(content=system_prompt),
            UserMessage(content=user_prompt)
        ]
        
        try:
            response = self.client.complete(
                messages=messages,
                model=self.model,
                temperature=0.7,
                max_tokens=800
            )
            
            return {
                "success": True,
                "tips": response.choices[0].message.content
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }


def print_banner():
    """Print welcome banner."""
    banner = """
    ╔════════════════════════════════════════════════════════════╗
    ║           🍳 Cooking AI Agent 🍳                           ║
    ║     Powered by GitHub Models - Your AI Cooking Assistant   ║
    ╚════════════════════════════════════════════════════════════╝
    """
    print(banner)


def print_menu():
    """Print main menu options."""
    menu = """
    Choose an option:
    
    1. 🔍 Search for recipes
    2. 📋 Extract ingredients from recipe
    3. 💡 Get cooking tips
    4. ❌ Exit
    """
    print(menu)


def get_user_input(prompt: str) -> str:
    """Get user input with prompt."""
    return input(f"\n{prompt}: ").strip()


def search_recipes_interactive(agent: CookingAIAgent):
    """Interactive recipe search."""
    print("\n" + "="*60)
    print("🔍 RECIPE SEARCH")
    print("="*60)
    
    query = get_user_input("What would you like to cook?")
    if not query:
        print("❌ Query cannot be empty.")
        return
    
    cuisine = get_user_input("Cuisine type (press Enter to skip)")
    dietary = get_user_input("Dietary restrictions (comma-separated, press Enter to skip)")
    
    dietary_list = [d.strip() for d in dietary.split(",")] if dietary else None
    
    print("\n🤖 Searching for recipes...\n")
    
    result = agent.search_recipes(
        query=query,
        cuisine=cuisine if cuisine else None,
        dietary_restrictions=dietary_list
    )
    
    if result["success"]:
        print("="*60)
        print(result["recipe"])
        print("="*60)
    else:
        print(f"❌ Error: {result['error']}")


def extract_ingredients_interactive(agent: CookingAIAgent):
    """Interactive ingredient extraction."""
    print("\n" + "="*60)
    print("📋 INGREDIENT EXTRACTION")
    print("="*60)
    
    print("\nPaste or type your recipe (press Enter twice when done):")
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            if lines and lines[-1] == "":
                break
            if not lines:
                break
            lines.append("")
    
    recipe_text = "\n".join(lines).strip()
    
    if not recipe_text:
        print("❌ Recipe text cannot be empty.")
        return
    
    print("\n🤖 Extracting ingredients...\n")
    
    result = agent.extract_ingredients(recipe_text)
    
    if result["success"]:
        print("="*60)
        print(result["ingredients"])
        print("="*60)
    else:
        print(f"❌ Error: {result['error']}")


def get_cooking_tips_interactive(agent: CookingAIAgent):
    """Interactive cooking tips."""
    print("\n" + "="*60)
    print("💡 COOKING TIPS")
    print("="*60)
    
    dish = get_user_input("What dish do you need tips for?")
    if not dish:
        print("❌ Dish name cannot be empty.")
        return
    
    print("\n🤖 Getting cooking tips...\n")
    
    result = agent.get_cooking_tips(dish)
    
    if result["success"]:
        print("="*60)
        print(result["tips"])
        print("="*60)
    else:
        print(f"❌ Error: {result['error']}")


def main():
    """Main application loop."""
    print_banner()
    
    # Initialize the AI agent
    try:
        agent = CookingAIAgent()
        print("✅ Successfully connected to GitHub Models API\n")
    except ValueError as e:
        print(f"❌ {e}")
        return
    except Exception as e:
        print(f"❌ Failed to initialize AI agent: {e}")
        return
    
    # Main interaction loop
    while True:
        print_menu()
        choice = get_user_input("Enter your choice (1-4)")
        
        if choice == "1":
            search_recipes_interactive(agent)
        elif choice == "2":
            extract_ingredients_interactive(agent)
        elif choice == "3":
            get_cooking_tips_interactive(agent)
        elif choice == "4":
            print("\n👋 Thank you for using Cooking AI Agent! Happy cooking!\n")
            break
        else:
            print("\n❌ Invalid choice. Please enter a number between 1 and 4.")
        
        input("\nPress Enter to continue...")
        print("\n" * 2)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye! Happy cooking!\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        sys.exit(1)
