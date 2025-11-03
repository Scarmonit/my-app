#!/usr/bin/env python3
"""
Example script demonstrating programmatic usage of the Cooking AI Agent.
This script shows how to use the CookingAIAgent class in your own applications.
"""

import os
from cooking_agent import CookingAIAgent


def example_recipe_search():
    """Example: Search for recipes."""
    print("="*60)
    print("Example 1: Recipe Search")
    print("="*60)
    
    agent = CookingAIAgent()
    
    # Simple search
    result = agent.search_recipes(query="chocolate cake")
    if result["success"]:
        print("\n🔍 Simple Recipe Search:")
        print(result["recipe"])
    
    # Search with cuisine filter
    result = agent.search_recipes(
        query="pasta",
        cuisine="Italian"
    )
    if result["success"]:
        print("\n🔍 Recipe Search with Cuisine Filter:")
        print(result["recipe"])
    
    # Search with dietary restrictions
    result = agent.search_recipes(
        query="tacos",
        dietary_restrictions=["vegetarian", "gluten-free"]
    )
    if result["success"]:
        print("\n🔍 Recipe Search with Dietary Restrictions:")
        print(result["recipe"])


def example_ingredient_extraction():
    """Example: Extract ingredients from a recipe."""
    print("\n" + "="*60)
    print("Example 2: Ingredient Extraction")
    print("="*60)
    
    agent = CookingAIAgent()
    
    recipe_text = """
    Classic Spaghetti Carbonara
    
    Ingredients:
    400g spaghetti
    200g pancetta or guanciale, diced
    4 large eggs
    100g Pecorino Romano cheese, grated
    Black pepper to taste
    Salt for pasta water
    
    Instructions:
    1. Cook spaghetti in salted boiling water until al dente
    2. Meanwhile, fry pancetta until crispy
    3. Beat eggs with grated cheese
    4. Drain pasta, mix with pancetta, then add egg mixture off heat
    5. Toss quickly and serve with black pepper
    """
    
    result = agent.extract_ingredients(recipe_text)
    if result["success"]:
        print("\n📋 Extracted Ingredients:")
        print(result["ingredients"])


def example_cooking_tips():
    """Example: Get cooking tips."""
    print("\n" + "="*60)
    print("Example 3: Cooking Tips")
    print("="*60)
    
    agent = CookingAIAgent()
    
    result = agent.get_cooking_tips("risotto")
    if result["success"]:
        print("\n💡 Cooking Tips for Risotto:")
        print(result["tips"])


def main():
    """Run all examples."""
    print("\n" + "="*60)
    print("Cooking AI Agent - Programmatic Usage Examples")
    print("="*60)
    
    # Check if token is available
    if not os.environ.get("GITHUB_TOKEN"):
        print("\n❌ Error: GITHUB_TOKEN environment variable not set")
        print("Please set your GitHub token:")
        print("  export GITHUB_TOKEN=your_token_here")
        return
    
    try:
        # Run examples
        example_recipe_search()
        example_ingredient_extraction()
        example_cooking_tips()
        
        print("\n" + "="*60)
        print("✅ All examples completed successfully!")
        print("="*60)
        
    except Exception as e:
        print(f"\n❌ Error running examples: {e}")


if __name__ == "__main__":
    main()
