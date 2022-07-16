from mysqlconnection import connectToMySQL
from flask import flash

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#this allows for    OOP to be implemented in the show function
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod #will get all info from database
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("users2").query_db(query) #this connects to schema
        # data comng back is list of dictionaries
        #translating to user objects:
        users = []
        for u in results: #u is a row of user
            users.append(cls(u))
        return users


#this will set up for new users to be added
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        result = connectToMySQL("users2").query_db(query,data)
        return result

#this will grab id and take you to edit screen
    @classmethod
    def get_one(cls,data):
        query= "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL("users2").query_db(query,data)
        return cls(result[0]) #result is a list 

#this will allow for update
    @classmethod
    def update(cls,data):
        query = "Update users SET first_name = %(first_name)s, last_name = %(last_name)s,email = %(email)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('users2').query_db(query,data)

#sql to destroy a datapoint
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM users WHERE id= %(id)s;"
        return connectToMySQL('users2').query_db(query,data)




