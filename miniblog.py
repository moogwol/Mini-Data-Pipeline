from flask import Flask, request, render_template, redirect, url_for
from snowplow_tracker import Tracker, Emitter

app = Flask(__name__)

e = Emitter("192.168.1.105:9090") # Replace this IP with the IP of your emitter
t = Tracker(e)

headings = [{'title': 'Local Mountain Bike Routes', 'url': 'routes'},
            {'title': 'Cat Stuck Up Tree', 'url': 'cat_tree'},
            {'title': 'Man enjoys Ice Cream', 'url': 'ice_man'}
            ]

@app.route('/')
def index():
    # t.track_page_view(page_url='http://127.0.0.1:5000/',  page_title='Index page')
    return render_template('index.html', headings=headings)

@app.route('/user/<username>')
def show_profile(username):
    return f'User {username}'

@app.route('/index')
def go_to_index():
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return 'This is not the page you are looking for', 404


@app.route('/routes')
def routes():
    # t.track_page_view(page_url='http://127.0.0.1:5000/routes' ,page_title='Local Mountain Biking Routes')
    return render_template('routes.html')

@app.route('/cat-tree')
def cat_tree():
    # t.track_page_view(page_url='http://127.0.0.1:5000/cat-tree' ,page_title='Cat stuck up tree')
    return render_template('cat-tree.html')

@app.route('/ice-man')
def ice_man():
    # t.track_page_view(page_url='http://127.0.0.1:5000/ice-man' ,page_title='Man Enjoys Ice Cream')
    return render_template('ice-man.html')