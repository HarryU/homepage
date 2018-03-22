import os
import sqlite3
from flask import *
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'resume.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='password'
))
app.config.from_envvar('RESUME_SETTINGS', silent=True)

def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    init_db()
    print('Initialised database')

def get_db():
    if not hasattr(g, 'sqlite _db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

def add_user(username, password):
    usernames = get_existing_usernames(get_db())
    if username not in usernames:
        hashed_password = generate_password_hash(password)
        db.execute('insert into users (username, passwd_hash) values (?, ?)',
                   [username, hashed_password])
        db.commit()
        flash('New user {} created.'.format(username))
    else:
        flash('User {} already exists.'.format(username))

def get_existing_usernames(db):
    cur = db.execute('select username from users')
    return cur.fetchall()

def get_hashed_password(db, username):
    cur = db.execute('select passwd_hash from users where username=?', [username])
    flash(cur)
    return cur.fetchall()

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    usernames = get_existing_usernames(get_db())
    if request.method == 'POST':
        username = request.form['username']
        if username in usernames:
            hashed_password = get_hashed_password(username)
            if check_password_hash(hashed_password, request.form['password']):
                session['logged_in'] = True
                flash('Logged in as {}'.format(username))
                return redirect(url_for(index))
    return render_template('login.html', error=error)

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def index():
    return render_template('about.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')

@app.route('/automatedinspection')
def automatedinspection():
    return render_template('automatedinspection.html')

@app.route('/autonomousboat')
def autonomousboat():
    return render_template('autonomousboat.html')

@app.route('/highspeedtracking')
def highspeedtracking():
    return render_template('highspeedtracking.html')
