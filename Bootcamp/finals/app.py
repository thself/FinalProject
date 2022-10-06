from flask import Flask, jsonify, render_template
from flask-sqlalchemy import SQLAlchemy

app = Flask (__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'

db = SQLAlchemy(app)
class Students(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))
   addr = db.Column(db.String(200))
   pin = db.Column(db.String(10))

def __init__(self, name, city, addr,pin):
   self.name = name
   self.city = city
   self.addr = addr
   self.pin = pin

db.create_all()
# Inserts records into a mapping table
db.session.add (model object)
# delete records from a table
db.session.delete (model object)
# retrieves all records (corresponding to SELECT queries) from the table.
model.query.all ()
@app.route('/')
def show_all():
   return render_template('show_all.html', students = students.query.all() )
"""
@app.route('/')
def index():
    return 'hello world'
"""

app = Flask (__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'

@app.route('/home')
def home():
    return '<h1>You are on the home page!</h1>'



@app.route('/json')
def json():
    return jsonify({'key' : 'value', 'listkey' : [1,2,3,4]})


if __name__ == '__main__':
    app.run()