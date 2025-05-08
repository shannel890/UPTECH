from app import app,db
from flask import render_template,redirect,url_for,flash
from app.forms import Loginform 
from app.models import User

@app.route('/')
def home():
    return render_template('index.html', title='KIPPS MALL')

@app.route('/rolex')
def rolex():
    return render_template('rolex.html', title='KIPPS MALL')

@app.route('/dior')
def dior():
    return render_template('dior.html', title='KIPPS MALL')

@app.route('/adidas')
def adidas():
    return render_template('adidas.html', title='KIPPS MALL')

@app.route('/samsung')
def samsung():
    return render_template('samsung.html', title='KIPPS MALL')

@app.route('/cart')
def cart():
    return render_template('cart.html', title='KIPPS MALL')



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Loginform()
   
@app.route('/logout')
def logout():
    flash('You have been logged out.')
    return redirect(url_for('home'))
    
