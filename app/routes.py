from flask import render_template
from app import app

@app.route('/')
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