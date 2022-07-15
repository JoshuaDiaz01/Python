from ast import Return
from flask import Flask, render_template, request, redirect

from users import User
app = Flask(__name__)

@app.route("/")
def index():
    return redirect('/users')


#this will get data from already lsited users in sql
@app.route('/users')
def users():
    return render_template('users.html', users=User.get_all())


#this will render to html
@app.route('/user/new')
def new():
    return render_template('users_two.html')


#this will create new user
@app.route('/user/create', methods =['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')

@app.route('/user/edit/<int:id>')
def edit(id):
    data = {
        "id" :id #this grabs the id from data 
    }
    return render_template("users_three.html", user = User.get_one(data))

#will execute the update and redirect
@app.route('/user/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')


#will enact the delete button
@app.route('/user/destroy/<int:id>')
def destroy(id): #specific to id so must take in id
    data = {
        'id': id
    }
    User.destroy(data)
    return redirect('/users')

#this is showing our users name
@app.route('/user/show/<int:id>')
def show(id):
    data = {
        "id" :id #this grabs the id from data 
    }
    return render_template("users_four.html", user = User.get_one(data))




if __name__ == "__main__":
    app.run(debug=True)
