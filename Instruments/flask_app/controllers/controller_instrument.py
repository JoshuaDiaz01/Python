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
    #validations
    if not model_instrument.Instrument.validator(request.form):
        return redirect('/instrument/new')

    #create instrument
    data = {
        **request.form,
        'user_id': session['uuid']
    }
    model_instrument.Instrument.create(data)
    return redirect('/')


#calling and displaying info
@app.route('/instrument/<int:id>')
def instrument_show(id):
    return render_template('instrument_show.html')


#calling page with form for modification on form
@app.route('/instrument/<int:id>/edit')
def instrument_edit(id):
    context = {
        'instrument' :model_instrument.Instrument.get_one({'id': id})
    }
    return render_template('instrument_edit.html', **context)


#does the UPDATING
@app.route('/instrument/<int:id>/update', methods = ['POST'])
def instrument_update(id):
    #VALIDATIONS
    if not model_instrument.Instrument.validator(request.form):
        return redirect(f'/instrument/{id}/edit')
#if it passes validation, call it
    data = {
        **request.form,
        'id':id
    }
    model_instrument.Instrument.update_one({data})
    return redirect(f'/instrument/{id}/edit')


#deleting name
@app.route('/instrument/<int:id>/delete')
def instrument_delete(id):
    data = {
        'id' : id
    }
    model_instrument.Instrument.delete_one(data)
    return redirect('/')
