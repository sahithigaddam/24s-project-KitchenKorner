from faker import Faker
import random

fake = Faker()

def generate_users(n=45):
    users = []
    for _ in range(n):
        user = {
            'User_ID': fake.user_id(),
            'Username': fake.username(),
            'Email': fake.email(),
            'Full_Name': fake.full_name(),
            'Created_At': fake.date_time()
        }
        users.append(user)
    return users

def generate_recipes(n=45):
    recipes = []
    for _ in range(n):
        recipe = {
            'Instructions': fake.instructions(), 
            'Image': fake.image(),  
            'Meal_Type': fake.meal_type(), 
            'Recipe_ID': fake.recipe_id(),
            'Post_ID': fake.post_id(), 
            'Cuisine': fake.cuisine(), 
            'Expected_Time': fake.expected_time(), 
            'Expected_Difficulty': fake.expected_difficulty()
        }
        recipes.append(recipe)
    return recipes

def generate_external_messages(n=45):
    external_messages = []
    for _ in range(n):
        message = {
            'user_id': fake.user_id(),
            'message': fake.message()
        }
        external_messages.append(message)
    return external_messages    

def generate_direct_messages(n=45)

