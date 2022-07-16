from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User: 
    db_name = "dojo_login"
    def __init__(self, db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.email = db_data['email']
        self.password = db_data['password']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

#create class method to save the users into database
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password,created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL(cls.db_name).query_db(query,data)

#appending users into the table
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db_name).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

#selecting user by id
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id= %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query)
        if len(results) < 1:
            return False
        return User(results[0])
    
#selecting user by email for the login page
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email= %(email)s;"
        results = connectToMySQL(cls.db_name).query_db(query)
        if len(results) < 1:
            return False
        return User(results[0])
    

#statiic method for checking if user is valid to register

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) < 3:
            is_valid = False
            flash("First name must be at least 3 characters.", "register")
        if len(user['last_name']) < 3:
            is_valid = False
            flash("Last name must be at least 3 characters.", "register")
        if not EMAIL_REGEX.match(user['email']):
            is_valid = False
            flash("Password must be at least 8 characters.", "register")
        if user['password'] != user['confirm']:
            is_valid = False
            flash("Passwords do not match.", "register")

        return is_valid
        