from flask import render_template, request
from app import app
from led_encoder import encode, read_sw


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/led_encode', methods=['POST'])
def led_encode():
    number = int(request.form['number'])
    return encode(number)


@app.route('/switch', methods=['GET'])
def switch():
    return read_sw()

