from app import app,db
from flask import render_template, redirect, url_for, flash, request
from app.forms import Loginform,Userform
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

@app.route('/user')
def user():
    users = User.query.all()
    return render_template('user.html', title='KIPPS MALL', users=users)

@app.route('/register',methods=['GET','POST'])
def register():
    form = Userform()
    
    if request.method == 'POST':
        username = request.form['username']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']

        new_user = User(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash(f'Registration for {new_user.username} successful! You can now log in.')
        return redirect(url_for('login'))
    return render_template('register.html', title='KIPPS MALL',reg_form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Loginform()
    flash(f'you are now successful logged in.')
    return render_template('login.html', form=form)
@app.route('/logout')
def logout():
    flash('You have been logged out.')
    return redirect(url_for('home'))
    
