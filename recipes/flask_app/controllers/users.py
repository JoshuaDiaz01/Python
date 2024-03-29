from flask import render_template, session, redirect, request, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_app import app 
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

#create
@app.route("/register", methods = ["POST"])
def register():
    if not User.get_by_email(request.form):
        if not User.validate(request.form):
            return redirect("/")
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print(pw_hash)
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': pw_hash
        }
        user_id = User.save(data)
        session['user_id'] = user_id 
        return redirect("/recipes")
    flash("Email already used!")
    return redirect('/')

@app.route("/login", methods = ["POST"])
def login():
    data = {"email": request.form["email"]}
    user = User.get_by_email(data)

    if not user:
        flash("Invalid email/password")
        return redirect('/')

    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid email/password")
        return redirect('/')

    session['user_id'] = user.id
    return redirect('/recipes')

#read
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recipes')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {"id": session['user_id']}
    user = User.get_one(data)
    recipes = Recipe.get_all()
    return render_template('recipes.html', user = user, recipes = recipes)

@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")
    