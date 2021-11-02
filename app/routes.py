from flask import render_template, redirect, flash, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
def home():
    return render_template('base.html', title='Welcome')

@app.route('/index')
def index():
    user = {'username':'Qifeng'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in New York!'
        },
        {
            'author': {'username': 'Serene'},
            'body': 'Want to go for a trip!'
        }
    ]
    return render_template('index.html',title = 'Home', user = user, posts = posts)

@app.route('/login', methods = ['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login request for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect(url_for('index'))
    return render_template('login.html', title = 'Sign In', form = form)