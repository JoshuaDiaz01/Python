from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.emails import Email


@app.route('/')
def index():
    return render_template("index.html")

#checking if the email is valid, calls on html if not valid
@app.route('/process',methods=['POST'])
def process():
    if not Email.is_valid(request.form):
        return redirect('/') #if false it will return error
    Email.save(request.form) # if true it will save the request
    return redirect('/results')


@app.route('/results')
def results():
    return render_template("results.html",emails = Email.get_all())


# this will route the destroy method once the delete is cliked
@app.route('/destroy/<int:id>')
def destroy_email(id):
    data = {
        "id": id
    }
    Email.destroy(data)
    return redirect('/results')