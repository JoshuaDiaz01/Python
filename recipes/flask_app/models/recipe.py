from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user


class Recipe:
    db_name = "recipes_schema"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name'] 
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30 = data['under_30']
        self.date_made = data['date_made']
        self.user_id = data['user_id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, under_30, date_made, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(under_30)s, %(date_made)s, %(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes LEFT JOIN users ON users.id = recipes.user_id;"
        results = connectToMySQL(cls.db_name).query_db(query)
        recipes = []
        for row in results:
            new_recipe = cls(row)
            user_data = {
                "id" : row['users.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'], 
                "email": row['email'],
                "password": row['password'],
            }
            new_user = user.User(user_data)
            new_recipe.owner = new_user
            recipes.append(new_recipe)
        return recipes
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        row = results[0]
        recipe = cls(row)
        user_data = {
            "id" : row['users.id'],
            "first_name": row['first_name'],
            "last_name": row['last_name'], 
            "email": row['email'],
            "password": row['password'],
        }
        new_user = user.User(user_data)
        recipe.owner = new_user
        return recipe

    @classmethod
    def edit(cls,data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, under_30 = %(under_30)s, date_made = %(date_made)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
        
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)


