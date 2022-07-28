from flask import render_template, session,redirect, request, flash
import re
from flask_bcrypt import Bcrypt
from flask_app import app

#this one will change
from flask_app.models import model_recipe
from flask_app.models import model_user

bcrypt = Bcrypt(app)

#create newsomething
@app.route('/recipe/new')
def recipe():
    return render_template('recipe_new.html')


#action to create in database
@app.route('/recipe/create', methods = ['POST'])
def recipe_create():
    #validations
    if not model_recipe.Recipe.validator(request.form):
        return redirect('/recipe/new')
    #create recipe
    data = {
        **request.form,
        'user_id': session['uuid']
    }
    model_recipe.Recipe.create(data)
    return redirect('/')


#calling and displaying info 
@app.route('/recipe/<int:id>')
def recipe_show(id):
    # id to show session id name
    data = {
        'id': id
    }
    recipe = model_recipe.Recipe.get_one(data)
    user = model_user.User.get_one({'id':session['uuid']})
    return render_template('recipe_show.html', recipe = recipe, user = user)


#calling page with form for modification on form
@app.route('/recipe/<int:id>/edit')
def recipe_edit(id):
    context = {
        'recipe' :model_recipe.Recipe.get_one({'id': id})
    }
    return render_template('recipe_edit.html', **context)


#does the UPDATING
@app.route('/recipe/<int:id>/update', methods = ['POST'])
def recipe_update(id):
    #VALIDATIONS
    if not model_recipe.Recipe.validator(request.form):
        return redirect(f'/recipe/{id}/edit')
#if it passes validation, call it
    data = {
        **request.form,
        'id':id
    }
    model_recipe.Recipe.update_one(data)
    return redirect('/')


#deleting name
@app.route('/recipe/<int:id>/delete')
def recipe_delete(id):
    data = {
        'id' : id
    }
    model_recipe.Recipe.delete_one(data)
    return redirect('/')
