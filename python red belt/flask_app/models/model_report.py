from ftplib import all_errors
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_user
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

DATABASE = "sightings"


class Report: 
    def __init__(self, data):
        #add attributes per column in table
        self.id = data['id']
        self.location = data['location']
        self.description = data['description']
        self.date = data['date']
        self.num_of = data['num_of']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.player = {}

#create class method to save the Instrument into database
    @classmethod
    def create(cls,data:dict) -> int:
        #add all column names and all values
        query = "INSERT INTO reports (location, description, date, num_of, user_id) VALUES (%(location)s, %(description)s,%(date)s,%(num_of)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)



#selecting user by id to route in the view recipe (shows the user that posted)
    @classmethod
    def get_one(cls,data:dict) -> int:
        query = "SELECT * FROM reports JOIN users ON users.id = reports.user_id WHERE reports.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        dict = results[0]
        report = cls(dict)
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
        report.player = new_user
        return report



#appending reports into the table
    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM reports JOIN users ON users.id = reports.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_reports = []
            for dict in results:
                report = cls(dict)
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
                report.player = user
                all_reports.append(report)
            return all_reports
        return [] 

    @classmethod
    def update_one(cls, data:dict) -> None:
        #add columns = values for every column you want to change
        query = "UPDATE reports SET location = %(location)s, description = %(description)s,date = %(date)s,num_of = %(num_of)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_one(cls,data:dict):
        query = "DELETE FROM reports WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)


#statiic method for checking if instrument is valid to register
    @staticmethod
    def validator(data:dict) -> bool:
        is_valid = True
        if len(data['location']) < 1:
            flash("location must be at least 3 characters.", "err_reports_location")
            is_valid = False

        #location didnt match time_played
        if len(data['description']) < 1:
            flash("Time Played must be at least 3 characters.", "err_reports_description")
            is_valid = False
    
        if len(data['date']) < 3:
            flash("Time Played must be at least 3 characters.", "err_reports_date")
            is_valid = False
        
        if len(data['num_of']) < 1:
            flash("Time Played must be at least 3 characters.", "err_reports_num_of")
            is_valid = False

        # if len(data['date_made']) < 3:
        #     flash("Time Played must be at least 3 characters.", "err_reports_date_made")
        #     is_valid = False
        
        return is_valid
        