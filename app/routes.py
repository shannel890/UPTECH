from app import app
from flask import render_template


@app.route('/')
def home():
    return render_template('addidas.html')

@app.route('/rolex')
def addidas():
    return render_template('rolex.html')



