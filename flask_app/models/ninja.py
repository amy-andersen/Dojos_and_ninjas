# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the ninja table from the database

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    schema_name = "dojos_and_ninjas"

#insert a new ninja to the database 
    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas ( first_name , last_name, age, dojo_id, created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(age)s , %(dojo_id)s , NOW() , NOW() );"
        return connectToMySQL(cls.schema_name).query_db( query, data )

    @classmethod
    def get_ninja(cls,data):
        query  = "SELECT * FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL(cls.schema_name).query_db(query,data)
        #return the one ninja
        ninja = cls( result[0] )
        return ninja