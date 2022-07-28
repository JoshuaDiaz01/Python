from flask import render_template, session,redirect, request, flash
import re
from flask_bcrypt import Bcrypt
from flask_app import app

#this one will change
from flask_app.models import model_user

@app.route('/')
def index():
    if 'uuid' in session:
        return redirect('/dashboard')
    return render_template('index.html')

#checking if someone is logged in
@app.route('/dashboard')
def dashboard():
    if 'uuid' not in session:
        return redirect('/')
    context = {
        #session uuid should be the one thats already logged in
        'user': model_user.User.get_one({'id': session['uuid']})
    }
    return render_template('dashboard.html', **context)


