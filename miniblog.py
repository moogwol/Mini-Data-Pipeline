from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_profile(username):
    return f'User {username}'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return 'Used get'
    else:
        return 'Used post'

@app.route('/index')
def go_to_index():
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return 'Get Fucked!', 404