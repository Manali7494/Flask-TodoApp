# Import of flask
from flask import Flask

# Initialization
app = Flask(__name__) 

# App route 
@app.route('/')

# Index function
def index():
    return "Hello World"