from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///pythonflask.db', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        Base.metadata.create_all(engine)


def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            attempt = int(session.get('attempt'))
            if attempt == 2:
                flash("This is your last chance")
                # attempt += 1
                # session['attempt'] = attempt
            if attempt == 3:
                flash('You have been logged out.')
                abort(404)
            else:
                attempt += 1
                session['attempt'] = attempt
                error = 'Invalid Credentials. Please try again'
        else:
            session['logged_in'] = True
            flash('You were logged in.')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

def home():
    session['attempt'] = 1
    return render_template('index.html')  # render a template