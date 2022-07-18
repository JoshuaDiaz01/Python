from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.dojo import Dojo

#create dojo
@app.route('/dojos/create', methods =['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect("/dojos")

#read dojo
@app.route("/")
def index():
    return redirect("/dojos")

@app.route("/dojos")
def dojos():
    # calling get all function to get objects 
    dojos = Dojo.get_all()
    return render_template("dojos.html", dojos = dojos)

@app.route("/dojos/<int:id>")
def show(id):
    #have to do data input bc there is no input in the html for a name statement
    data = {"id": id}
    dojos = Dojo.get_dojo_with_ninjas(data)
    return render_template("show_dojo.html", dojos = dojos)
