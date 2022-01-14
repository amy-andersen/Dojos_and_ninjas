from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
#form to create a new ninja 
def create_ninja():
    return render_template('new_ninja.html', dojos=Dojo.get_all())

@app.route('/new_ninja', methods=["POST"])
#post method to add a new ninja
#redirect to /dojo/id page
def new_ninja():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    new_ninja_id = Ninja.save(data)
    data = {
        "id": new_ninja_id
    }
    new_ninja = Ninja.get_ninja(data)
    return redirect(f'/dojo/{new_ninja.dojo_id}')