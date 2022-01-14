# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja
# model the class after the dojo table from the database

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    schema_name = "dojos_and_ninjas"

#return all dojos from database 
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
#call the connectToMySQL function with the target schema
        results = connectToMySQL(cls.schema_name).query_db(query)
# Create an empty list to append instances of dojos
        dojos = []
# Iterate over the db results and create instances of dojos with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

#insert a new dojo to the database 
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos ( name , created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
        return connectToMySQL(cls.schema_name).query_db( query, data )

#return one dojo from database with all the associated ninjas
    @classmethod
    def get_dojo_with_ninjas(cls,data):
        query  = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        result = connectToMySQL(cls.schema_name).query_db(query,data)
        #return the one dojo
        dojo = cls( result[0] )
        #return all associated ninjas
        for row_from_db in result:
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"],
                "dojo_id": row_from_db["dojo_id"]
            }
            dojo.ninjas.append( Ninja(ninja_data) )
        return dojo