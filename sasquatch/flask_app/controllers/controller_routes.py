from flask import render_template, session,redirect, request, flash
import re
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models import model_report

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
    #context will be able to call all recipes
    user_data ={
        'id': session['uuid']
    }
    #user_data is defined to access session id in dashboard html
    context = {
        'all_reports': model_report.Report.get_all(),
        'user': model_user.User.get_one(user_data)
        
    }
    return render_template('dashboard.html', **context)

#checking if someone is logged in
@app.route('/report_new')
def report_new():
    if 'uuid' not in session:
        return redirect('/')
    #context will be able to call all reports
    user_data ={
        'id': session['uuid']
    }
    #user_data is defined to access session id in report_new html
    context = {
        # 'all_reports': model_report.Report.get_all(),
        'user': model_user.User.get_one(user_data)
        
    }
    return render_template('report_new.html', **context)

# @app.route('/report/<int:id>edit')
# def report_edit():
#     if 'uuid' not in session:
#         return redirect('/')
#     #context will be able to call all reports
#     user_data ={
#         'id': session['uuid']
#     }
#     #user_data is defined to access session id in report_new html
#     context = {
#         # 'all_reports': model_report.Report.get_all(),
#         'user': model_user.User.get_one(user_data)
        
#     }
#     return render_template('report_new.html', **context)