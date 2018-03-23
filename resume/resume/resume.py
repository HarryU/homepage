import os
import sqlite3
from flask import *
from werkzeug.security import generate_password_hash, check_password_hash

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
    db = get_db()
    username_exists = db.execute('select exists(select 1 from users where username=? limit 1)', [username]).rowcount == 1
    if not username_exists:
        hashed_password = generate_password_hash(password)
        db.execute('insert into users (username, passwd_hash) values (?, ?)', [username, hashed_password])
        db.commit()
        print('New user "{}" created.'.format(username))
    else:
        print('User "{}" already exists.'.format(username))

def remove_user(username):
    db = get_db()
    db.execute('delete from users where username=?', [username])
    db.commit()
    print('deleted user "{}"'.format(username))


def get_existing_usernames(db):
    cur = db.execute('select username from users')
    return cur.fetchall()

def get_hashed_password(db, username):
    cur = db.execute('select passwd_hash from users where username=?', [username])
    return cur.fetchone()

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        db = get_db()
        username = request.form['username']
        username_exists = len(db.execute('select exists(select 1 from users where username=?)', [username]).fetchall()) > 0
        if username_exists:
            hashed_password = get_hashed_password(db, username)[0]
            password = request.form['password']
            password_matches = check_password_hash(hashed_password, password)
            if password_matches:
                session['logged_in'] = True
                flash('Logged in as {}'.format(username))
                return redirect(url_for('index'))
            else:
                error = "Invalid password for user {}".format(username)
        else:
            error = "Invalid username {}".format(username)
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You have been logged out.')
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('about.html')

@app.route('/startpage')
def startpage():
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    return render_template('startpage.html')

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

@app.route('/blog')
def blog():
    db = get_db()
    cur = db.execute('select title, text from blogposts order by id desc')
    entries = cur.fetchall()
    return render_template('blog.html', entries=entries)

@app.route('/blog/new', methods=['POST'])
def new_post():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    title = request.form['title']
    text = request.form['text']
    db.execute('insert into blogposts (title, text) values (?, ?)', [title, text])
    db.commit()
    flash('New post "{}" added to blog'.format(title))
    return redirect(url_for('blog'))
