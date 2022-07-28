from flask import render_template, session,redirect, request, flash
import re
from flask_bcrypt import Bcrypt
from flask_app import app

#this one will change
from flask_app.models import model_pet

bcrypt = Bcrypt(app)

#create newsomething
@app.route('/pet/new')
def pet():
    return render_template('pet_new.html')


#action to create in database
@app.route('/pet/create', methods = ['POST'])
def pet_create():

        #create instrument
    data = {
        **request.form,
        'user_id': session['uuid']
    }
    model_pet.Pets.create(data)
    return redirect('/')



#calling and displaying info
@app.route('/pet/<int:id>')
def pet_show(id):
    return render_template('pet_show.html')


#calling page with form for modification on form
@app.route('/pet/<int:id>/edit')
def pet_edit(id):
    return render_template('pet_edit.html')


# #does the editing
# @app.route('/pet/<int:id>/create')
# def pet_create(id):
#     return redirect('/')


#deleting name
@app.route('/pet/<int:id>/delete')
def user_delete(id):
    return redirect('/')
