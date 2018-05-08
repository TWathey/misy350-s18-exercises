import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy(app)

#define database tables
class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    about = db.Column(db.Text)


@app.route('/')
def index():
        # return "hello world"
        return render_template('index.html')

@app.route('/users/<string:username>')
def users(username):
    # return "<h1>hello %s</h1>" % usernamew
    return render_template('user.html', uname=username)
@app.route('/user')
def user():
    return "this is the page for users"


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == "GET":
        # return "hello GET"
        return render_template('form.html')
    if request.method == "POST":
        first_name = request.form["first_name"]
        return "Hi, your nme is %s" % first_name

if __name__ == '__main__':
    app.run()
