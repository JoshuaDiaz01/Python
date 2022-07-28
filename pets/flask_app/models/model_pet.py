from ftplib import all_errors
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
from flask_app.models import model_user
DATABASE = "pets_db"


class Pets: 
    def __init__(self, data):
        #add attributes per column in table
        self.id = data['id']
        self.name = data['name']
        self.height = data['height']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data ['user_id']
        self.player = {}

#create class method to save the pets into database
    @classmethod
    def create(cls,data:dict) -> int:
        #add all column names and all values
        query = "INSERT INTO pets (name, height, age, user_id) VALUES (%(name)s, %(height)s,%(age)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

#appending instruments into the table
    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM pets JOIN users ON users.id = pets.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_pets = []
            for dict in results:
                pet = cls(dict)
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
                pet.player = user
                all_pets.append(pet)
            return all_pets
        return [] 


#selecting user by id
    @classmethod
    def get_one(cls,data:dict) -> int:
        query = "SELECT * FROM pets WHERE id= %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:
            return cls(results[0])
        return False

#selecting user by id
    @classmethod
    def get_one_by_email(cls,data:dict) -> int:
        query = "SELECT * FROM pets WHERE id= %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:
            return cls(results[0])
        return False

#appending pets into the table
    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM pets;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_pets = []
            for pets_single in results:
                all_pets.append(cls(pets_single))
            return all_pets
        return False

    @classmethod
    def update_one(cls, data:dict) -> None:
        #add columns = values for every column you want to change
        query = "UPDATE pets SET column_name = %(column_name)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_one(cls,data:dict) -> None:
        query = "UPDATE pets SET column_name= %(column_name)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)


#statiic method for checking if instrument is valid to register
    @staticmethod
    def validator(data:dict) -> bool:
        is_valid = True
        if len(data['name']) < 1:
            flash("name must be at least 3 characters.", "err_pets_name")
            is_valid = False

        #name didnt match time_played
        if len(data['height']) < 1:
            flash("Time Played must be at least 3 characters.", "err_pets_height")
            is_valid = False
    
        if len(data['age']) < 1:
            flash("Time Played must be at least 3 characters.", "err_pets_age")
            is_valid = False
        
        return is_valid
        