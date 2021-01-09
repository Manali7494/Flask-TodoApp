# Import of flask
from flask import Flask, render_template

# Initialization
app = Flask(__name__) 

# App route 
@app.route('/')

# Index function
def index():
    return render_template('base.html') # render template

# Using 'python app.py' - Alternate way of running the app using 
if __name__ == "__main__":
    app.run(debug=True)