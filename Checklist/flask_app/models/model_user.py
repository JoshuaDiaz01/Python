from ftplib import all_errors
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

DATABASE = "scheme_name_here"


class table_name: 
    def __init__(self, data):
        #add attributes per column in table
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#create class method to save the table_name into database
    @classmethod
    def create(cls,data:dict) -> int:
        #add all column names and all values
        query = "INSERT INTO table_name (column) VALUES (%(value_name)s);"
        return connectToMySQL(DATABASE).query_db(query,data)



#selecting user by id
    @classmethod
    def get_one(cls,data:dict) -> int:
        query = "SELECT * FROM table_name WHERE email= %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:
            return cls(results[0])
        return False

#selecting user by id
    @classmethod
    def get_one_by_email(cls,data:dict) -> int:
        query = "SELECT * FROM table_name WHERE id= %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:
            return cls(results[0])
        return False

#appending table_name into the table
    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM table_name;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_table_name = []
            for table_name_single in results:
                all_table_name.append(cls(table_name_single))
            return all_table_name
        return False

    @classmethod
    def update_one(cls, data:dict) -> None:
        #add columns = values for every column you want to change
        query = "UPDATE table_name SET column_name = %(column_name)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_one(cls,data:dict) -> None:
        query = "UPDATE table_name SET column_name= %(column_name)s WEHRE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)


#statiic method for checking if user is valid to register
    @staticmethod
    def validator(data:dict) -> bool:
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
        