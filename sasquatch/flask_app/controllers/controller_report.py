from flask import render_template, session,redirect, request, flash
import re
from flask_bcrypt import Bcrypt
from flask_app import app

#this one will change
from flask_app.models import model_report
from flask_app.models import model_user

bcrypt = Bcrypt(app)

#create newsomething
@app.route('/report/new')
def report():
        # id to show session id name
    user_data = {
        'id': session['uuid']
    }
    user = model_user.User.get_one({'id':session['uuid']})
    return render_template('report_new.html', user_data = user_data, user = user)



#action to create in database
@app.route('/report/create', methods = ['POST'])
def report_create():
    #validations
    if not model_report.Report.validator(request.form):
        return redirect('/report/new')
    #create report
    data = {
        **request.form,
        'user_id': session['uuid']
    }
    model_report.Report.create(data)
    return redirect('/')


#calling and displaying info 
@app.route('/report/<int:id>')
def report_show(id):
    # id to show session id name
    user_data = {
        'id': id
    }
    report = model_report.Report.get_one(user_data)
    user_data = model_user.User.get_one({'id':session['uuid']})
    return render_template('report_show.html', report = report, user_data = user_data)


#calling page with form for modification on form
# @app.route('/report/<int:id>/edit')
# def report_edit(id):
#     context = {
#         'report' :model_report.Report.get_one({'id': id})
#     }
#     return render_template('report_edit.html', **context)

@app.route('/report/<int:id>/edit', methods = ['POST'])
def report_edit(id):
    #VALIDATIONS
    if not model_report.Report.validator_report(request.form):
        return redirect(f'/report/{id}/edit')
#if it passes validation, call it
    data = {
        **request.form,
        'id':id
    }
    model_report.Report.update_one(data)
    return redirect('/')

#does the UPDATING
@app.route('/report/<int:id>/update', methods = ['POST'])
def report_update(id):
    #VALIDATIONS
    if not model_report.Report.validator(request.form):
        return redirect(f'/report/{id}/edit')
#if it passes validation, call it
    data = {
        **request.form,
        'id':id
    }
    model_report.Report.update_one(data)
    return redirect('/')


#deleting name
@app.route('/report/<int:id>/delete')
def report_delete(id):
    data = {
        'id' : id
    }
    model_report.Report.delete_one(data)
    return redirect('/')
