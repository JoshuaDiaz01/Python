from flask import render_template, session,redirect, request, flash
import re
from flask_bcrypt import Bcrypt
from flask_app import app

#this one will change
from flask_app.models import model_table_name

bcrypt = Bcrypt(app)

#create newsomething
@app.route('/table_name/new')
def table_name():
    return render_template('table_name_new.html')


#action to create in database
@app.route('/table_name/create', methods = ['POST'])
def table_name_create():
    return redirect('/')


#calling and displaying info
@app.route('/table_name/<int:id>')
def table_name_show(id):
    return render_template('table_name_show.html')


#calling page with form for modification on form
@app.route('/table_name/<int:id>/edit')
def table_name_edit(id):
    return render_template('table_name_edit.html')


#does the editing
@app.route('/table_name/<int:id>/create')
def table_name_create(id):
    return redirect('/')


#deleting name
@app.route('/table_name/<int:id>/delete')
def table_name_delete(id):
    return redirect('/')
