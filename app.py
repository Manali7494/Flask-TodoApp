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

# App route 
@app.route('/')

# Index function
def index():
    return render_template('base.html') # render template

# Using 'python app.py'
if __name__ == "__main__":
    #Creating database
    db.create_all()
    # Running app in development
    app.run(debug=True)