import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *

engine = create_engine('sqlite:///pythonflask.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

user = User("admin", "password")
session.add(user)

user = User("python", "python")
session.add(user)

user = User("jumpiness", "python")
session.add(user)


def add_user(username, password):
    user = User(username, password)
    session.add(user)
    session.commit()


# commit the record the database
session.commit()

session.commit()
