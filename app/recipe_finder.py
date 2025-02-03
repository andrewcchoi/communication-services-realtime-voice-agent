from thefuzz import fuzz
from thefuzz import process


class RecipeFinder:

    @classmethod
    def find_recipe(cls, ingredients):
        ingredients_set = set(map(str.lower, ingredients))  # Normalize input

        best_match = None
        max_score = 0  # Tracks the best fuzzy match score

        for recipe_name, recipe_data in cls.top_recipes.items():
            recipe_ingredients = set(map(str.lower, recipe_data["ingredients"]))  # Normalize recipe ingredients
            total_score = 0  # Aggregate match score for this recipe

            for input_ingredient in ingredients_set:
                best_match_score = max(
                    [fuzz.partial_ratio(input_ingredient, recipe_ingredient) 
                     for recipe_ingredient in recipe_ingredients], 
                    default=0
                )
                total_score += best_match_score  # Sum up scores for the recipe

            if total_score > max_score:
                max_score = total_score
                best_match = (recipe_name, recipe_data)

        return best_match

    # https://www.allrecipes.com/longform/top-10-recipes-of-all-time/

    top_recipes = {
        "World's Best Lasagna": {
            "url": "https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/",
            "ingredients": [
                "sweet Italian sausage",
                "lean ground beef",
                "onion",
                "garlic",
                "crushed tomatoes",
                "tomato paste",
                "tomato sauce",
                "water",
                "sugar",
                "dried basil leaves",
                "fennel seeds",
                "Italian seasoning",
                "salt",
                "black pepper",
                "fresh parsley",
                "lasagna noodles",
                "ricotta cheese",
                "egg",
                "mozzarella cheese",
                "Parmesan cheese",
            ],
        },
        "Banana Banana Bread": {
            "url": "https://www.allrecipes.com/recipe/20144/banana-banana-bread/",
            "ingredients": [
                "ripe bananas",
                "melted butter",
                "white sugar",
                "egg",
                "vanilla extract",
                "baking soda",
                "salt",
                "all-purpose flour",
            ],
        },
        "Homemade Mac and Cheese": {
            "url": "https://www.allrecipes.com/recipe/11679/homemade-mac-and-cheese/",
            "ingredients": [
                "elbow macaroni",
                "butter",
                "all-purpose flour",
                "salt",
                "black pepper",
                "milk",
                "shredded Cheddar cheese",
            ],
        },
        "Chicken Pot Pie IX": {
            "url": "https://www.allrecipes.com/recipe/26317/chicken-pot-pie-ix/",
            "ingredients": [
                "cubed skinless, boneless chicken breast",
                "sliced carrots",
                "frozen green peas",
                "sliced celery",
                "butter",
                "chopped onion",
                "all-purpose flour",
                "salt",
                "black pepper",
                "celery seed",
                "chicken broth",
                "milk",
                "unbaked pie crusts",
            ],
        },
        "Easy Meatloaf": {
            "url": "https://www.allrecipes.com/recipe/16354/easy-meatloaf/",
            "ingredients": [
                "ground beef",
                "egg",
                "onion",
                "milk",
                "bread crumbs",
                "salt",
                "black pepper",
                "brown sugar",
                "prepared mustard",
                "ketchup",
            ],
        },
        "Zuppa Toscana": {
            "url": "https://www.allrecipes.com/recipe/143069/zuppa-toscana/",
            "ingredients": [
                "bulk mild Italian sausage",
                "crushed red pepper flakes",
                "diced bacon",
                "onion",
                "garlic",
                "chicken broth",
                "water",
                "potatoes",
                "heavy cream",
                "fresh kale",
            ],
        },
        "Oven-Roasted Asparagus": {
            "url": "https://www.allrecipes.com/recipe/214931/oven-roasted-asparagus/",
            "ingredients": [
                "asparagus",
                "olive oil",
                "Parmesan cheese",
                "garlic",
                "salt",
                "black pepper",
                "lemon juice",
            ],
        },
        "Slow Cooker Pulled Pork": {
            "url": "https://www.allrecipes.com/recipe/228823/slow-cooker-pulled-pork/",
            "ingredients": [
                "pork shoulder roast",
                "bottled barbecue sauce",
                "apple cider vinegar",
                "chicken broth",
                "brown sugar",
                "yellow mustard",
                "Worcestershire sauce",
                "chili powder",
                "onion",
                "garlic",
                "thyme",
                "salt",
                "black pepper",
                "cayenne pepper",
                "hamburger buns",
            ],
        },
        "Baked Ziti I": {
            "url": "https://www.allrecipes.com/recipe/23600/baked-ziti-i/",
            "ingredients": [
                "ziti pasta",
                "onion",
                "lean ground beef",
                "garlic",
                "marinara sauce",
                "ricotta cheese",
                "mozzarella cheese",
                "egg",
                "grated Parmesan cheese",
            ],
        },
        "Banana Muffins II": {
            "url": "https://www.allrecipes.com/recipe/7067/banana-muffins-ii/",
            "ingredients": [
                "all-purpose flour",
                "baking powder",
                "baking soda",
                "salt",
                "ripe bananas",
                "white sugar",
                "egg",
                "melted butter",
            ],
        },
    }
