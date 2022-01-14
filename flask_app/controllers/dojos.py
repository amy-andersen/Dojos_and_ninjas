from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.dojo import Dojo

@app.route('/dojos')
#display all dojos and a form to add a new dojo
def dojos():
    return render_template('index.html', dojos=Dojo.get_all())

@app.route('/dojo/<int:id>')
#shows all the ninjas for a specific dojo
def show_dojo(id):
    data = {
        "id":id
    }
    return render_template('show_dojo.html', dojo=Dojo.get_dojo_with_ninjas(data))

@app.route('/new_dojo', methods=["POST"])
#post method to add a new dojo
#redirect to /dojos page
def new_dojo():
    data = {
        "name": request.form["name"]
    }
    Dojo.save(data)
    return redirect('/dojos')