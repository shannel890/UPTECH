from app import app
from flask import render_template
from app.forms import Loginform 

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
    return render_template('login.html', title='KIPPS MALL', form=form)