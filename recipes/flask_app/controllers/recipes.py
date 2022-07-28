from flask import render_template, session, redirect, request, flash
from flask_app.models.recipe import Recipe
from flask_app.models.user import User
from flask_app import app 


@app.route('/recipes/add/<int:id>', methods = ['POST'])
def create(id):
    data = {
        **request.form ,
        'user_id':id
    }
    Recipe.save(data)
    return redirect('/recipes/new')

@app.route("/recipes/new")
def create_page():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('add_recipe.html')

@app.route('/recipes/<int:id>')
def show(id):
    data = {
        'id': id
    }
    recipe = Recipe.get_one(data)
    user = User.get_one({'id':session['user_id']})
    return render_template('show_recipe.html', recipe = recipe, user = user)

@app.route("/recipes/edit/<int:id>")
def edit_page(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        **request.form ,
        'id': id
    }
    recipe = Recipe.get_one(data)
    if recipe.user_id != session['user_id']:
        flash("Thats not yours to edit")
        return redirect("/recipes")
    return render_template("edit.html", recipe = recipe)


@app.route('/update/<int:id>', methods = ['POST'])
def edit_recipe(id):
    data = {
        **request.form,
        'id': id
    }
    recipe = Recipe.get_one(data)
    if recipe.user_id != session['user_id']:
        flash("Thats not yours to edit")
        return redirect("/recipes")
    Recipe.edit(data)
    return redirect("/recipes")


@app.route("/delete/<int:id>")
def delete_recipe(id):
    data = {
        'id':id
    }
    recipe = Recipe.get_one(data)
    if recipe.user_id != session['user_id']:
        flash("WOAHHHH!!! What you doing there buddy? Thats a BIG NO NO!")
        return redirect("/recipes")
    Recipe.delete(data)
    return redirect('/recipes')

