from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
from dummy import add_user

engine = create_engine('sqlite:///pythonflask.db', echo=True)

app = Flask(__name__)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('user.html')


@app.route('/login', methods=['POST'])
def do_admin_login():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    loginsession = sessionmaker(bind=engine)
    s = loginsession()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]))
    result = query.first()

    if result:
        session['logged_in'] = True
    else:
        flash('wrong password')
    return home()


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    # POST_USERNAME = str(request.form['username'])
    # POST_PASSWORD = str(request.form['password'])
    #
    # loginsession = sessionmaker(bind=engine)
    # s = loginsession()
    # query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]))
    # result = query.first()
    #
    # if result:
    #     session['logged_in'] = True
    # else:
    #     flash('wrong password')
    # return home()

    # while

    return render_template('signup.html')

    # POST_USERNAME = str(request.form['username'])
    # POST_PASSWORD = str(request.form['password'])
    # d = add_user(POST_USERNAME, POST_PASSWORD)
    # if d:
    #     return render_template('login.html')


    # # engine.execute('INSERT INTO users '
    # #                '(username, password)' 'Values ='[POST_USERNAME][POST_PASSWORD] )
    # signupsession = sessionmaker(bind=engine)
    # s = signupsession()
    #
    # s.users(User).insert().values(User.username([POST_USERNAME]), User.password([POST_PASSWORD]))


@app.route('/logout')
def logout():
    session['logged_in'] = False
    return home()


# @app.route('/test')
# def test():
#     POST_USERNAME = "python"
#     POST_PASSWORD = "python"
#     Session = sessionmaker(bind=engine)
#     s = Session()
#     query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
#     result = query.first()
#     if request:
#         return "Object Found"
#     else:
#         return "object not found " + POST_USERNAME + " " + POST_PASSWORD


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)
