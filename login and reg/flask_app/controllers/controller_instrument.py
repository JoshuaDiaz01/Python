from flask import render_template, session,redirect, request, flash
import re
from flask_bcrypt import Bcrypt
from flask_app import app

#this one will change
from flask_app.models import model_instrument

bcrypt = Bcrypt(app)

#create newsomething
@app.route('/instrument/new')
def instrument():
    return render_template('instrument_new.html')


#action to create in database
@app.route('/instrument/create', methods = ['POST'])
def instrument_create():
    return redirect('/')


#calling and displaying info
@app.route('/instrument/<int:id>')
def instrument_show(id):
    return render_template('instrument_show.html')


#calling page with form for modification on form
@app.route('/instrument/<int:id>/edit')
def instrument_edit(id):
    return render_template('instrument_edit.html')


# #does the editing
# @app.route('/instrument/<int:id>/create')
# def instrument_create(id):
#     return redirect('/')


#deleting name
@app.route('/instrument/<int:id>/delete')
def user_delete(id):
    return redirect('/')
