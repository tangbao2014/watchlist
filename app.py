from flask import Flask,url_for,render_template
from flask_sqlalchemy import SQLAlchemy
import os
import click

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))

class Movie(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))

@app.cli.command()
@click.option('--drop',is_flag=True,help='Create after drop.')
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')

@app.cli.command()
def forge():
    db.create_all()
    name = 'tangbao'
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Three Colours trilogy', 'year': '1993'},
        {'title': 'Forrest Gump', 'year': '1994'},
        {'title': 'Perfect Blue', 'year': '1997'},
        {'title': 'The Matrix', 'year': '1999'},
        {'title': 'Memento', 'year': '2000'},
        {'title': 'The Bucket list', 'year': '2007'},
        {'title': 'Black Swan', 'year': '2010'},
        {'title': 'Gone Girl', 'year': '2014'},
        {'title': 'CoCo', 'year': '2017'},
    ]
    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'],year=m['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo('Done.')

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