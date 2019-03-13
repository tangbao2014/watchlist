from flask import Flask,url_for,render_template
app = Flask(__name__)

name = 'tangbao'

movies = [
    {'name': 'My Neighbor Totoro', 'year': '1988'},
    {'name': 'Three Colours trilogy', 'year': '1993'},
    {'name': 'Forrest Gump', 'year': '1994'},
    {'name': 'Perfect Blue', 'year': '1997'},
    {'name': 'The Matrix', 'year': '1999'},
    {'name': 'Memento', 'year': '2000'},
    {'name': 'The Bucket list', 'year': '2007'},
    {'name': 'Black Swan', 'year': '2010'},
    {'name': 'Gone Girl', 'year': '2014'},
    {'name': 'CoCo', 'year': '2017'},
]

@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)

@app.route('/user/<name>')
def user_page(name):
    return "User:%s"%name

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page',name='wangshixue'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for',num=2))
    return 'Test page'