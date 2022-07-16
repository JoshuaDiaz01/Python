from flask import render_template, session,redirect, request,flash
import re
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models.user import User

bcrypt = Bcrypt(app)

#home route
@app.route('/')
def index():
    return render_template('index.html')

#register route
@app.route('/register', methods = ['POST'])
def register():
    is_valid = User.validate_user(request.form)

    if not is_valid:
        return redirect('/')
    new_user = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"], 
        "email": request.form["email"],
        "password": request.form["password"]
    }
#creating session 
    id = User.save(new_user)
    session['user id'] = id
    return redirect('/dashboard')

#login route
@app.route('/login', methods = ['POST'])
def login():
#reaching in a library
    data = {
        'email': request.form['email']
    }
    user = User.get_by_email(data)
    print('************')
    # print(user.password)
    if not user:
        flash("Invalid email/password", "login")
        return redirect('/')

    if not bcrypt.check_password_hash(user.password,request.form['password']):
        flash("Invalid email/password", "login")
        return redirect('/')
    session['user_id']= user.id
    return redirect('/dashboard')

#dashboard route

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    user = User.get_one(data)
    # users = User.get_all()
    return render_template('dahsboard.html', user=user) #users=users)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')