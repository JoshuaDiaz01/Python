# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Friend:
    def __init__( self , data ):
        self.id = data['id'] #always include all your columns
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
    # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('first_flak').query_db(query) #first flask is database(schema), query db calls on other file and runs query function
    # Create an empty list to append our instances of friends
        friends = []
    # Iterate over the db results and create instances of friends with cls.
        for friend in results: #friend represents each dictionairy
            friends.append( cls(friend) ) #calling class passing in dict of friend, cls has to match with class name
        return friends
            



    @classmethod
    def save(cls, data ):
        query = "INSERT INTO friends ( first_name , last_name , occupation , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(occ)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('first_flak').query_db( query, data ) #quer_db is a built in
