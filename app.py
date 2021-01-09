# Import of flask
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialization
app = Flask(__name__) 

#Using sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Creating database
db = SQLAlchemy(app)


# Model Creation
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

# App route 
@app.route('/')

# Index function
def index():
    # query database for todos
    todo_list = Todo.query.all()

    print(todo_list)

    # render
    return render_template('base.html', todo_list=todo_list) # render template

@app.route('/add', methods=['POST'])
def add():

    # Get input fields from the form
    title = request.form.get("title")
    
    # Add to db
    new_todo = Todo(title = title, complete=False)
    db.session.add(new_todo)
    db.session.commit()

    return redirect(url_for("index"))

# Using 'python app.py'
if __name__ == "__main__":
    #Creating database
    db.create_all()

    # Running app in development
    app.run(debug=True)