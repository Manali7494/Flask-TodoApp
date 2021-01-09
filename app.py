# Import of flask
from flask import Flask, render_template
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

# Using 'python app.py'
if __name__ == "__main__":
    #Creating database
    db.create_all()

    #app new to do in database
    # new_todo = Todo(title = "todo 1", complete=False)
    # db.session.add(new_todo)
    # db.session.commit()

    # Running app in development
    app.run(debug=True)