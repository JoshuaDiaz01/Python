from ftplib import all_errors
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_user
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

DATABASE = "recipes"


class Recipe: 
    def __init__(self, data):
        #add attributes per column in table
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30 = data['under_30']
        self.date_made = data['date_made']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.player = {}

#create class method to save the Instrument into database
    @classmethod
    def create(cls,data:dict) -> int:
        #add all column names and all values
        query = "INSERT INTO recipes (name, description, instructions, under_30, date_made, user_id) VALUES (%(name)s, %(description)s,%(instructions)s,%(under_30)s,%(date_made)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)



#selecting user by id to route in the view recipe (shows the user that posted)
    @classmethod
    def get_one(cls,data:dict) -> int:
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        dict = results[0]
        recipe = cls(dict)
        user_data = {
            "id" : dict['users.id'],
            "first_name": dict['first_name'],
            "last_name": dict['last_name'], 
            "email": dict['email'],
            "pw": dict['pw'],
            'created_at': dict['users.created_at'],
            'updated_at': dict['users.updated_at'],
        }
        new_user = model_user.User(user_data)
        recipe.player = new_user
        return recipe



#appending recipes into the table
    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_recipes = []
            for dict in results:
                recipe = cls(dict)
                user_data = {
                    'id': dict['users.id'],
                    'created_at': dict['users.created_at'],
                    'updated_at': dict['users.updated_at'],
                    'first_name': dict['first_name'],
                    'last_name': dict['last_name'],
                    'email': dict['email'],
                    'pw': dict['pw'],
                }
                user = model_user.User(user_data)
                recipe.player = user
                all_recipes.append(recipe)
            return all_recipes
        return [] 

    @classmethod
    def update_one(cls, data:dict) -> None:
        #add columns = values for every column you want to change
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s,instructions = %(instructions)s,under_30 = %(under_30)s,date_made = %(date_made)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_one(cls,data:dict):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)


#statiic method for checking if instrument is valid to register
    @staticmethod
    def validator(data:dict) -> bool:
        is_valid = True
        if len(data['name']) < 1:
            flash("name must be at least 3 characters.", "err_recipes_name")
            is_valid = False

        #name didnt match time_played
        if len(data['description']) < 1:
            flash("Time Played must be at least 3 characters.", "err_recipes_description")
            is_valid = False
    
        if len(data['instructions']) < 3:
            flash("Time Played must be at least 3 characters.", "err_recipes_instructions")
            is_valid = False
        
        # if len(data['under_30']) < 3:
        #     flash("Time Played must be at least 3 characters.", "err_recipes_under_30")
        #     is_valid = False

        if len(data['date_made']) < 3:
            flash("Time Played must be at least 3 characters.", "err_recipes_date_made")
            is_valid = False
        
        return is_valid
        