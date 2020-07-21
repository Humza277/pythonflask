from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Welcome to my Flask project</h1>"


@app.route("/welcome_user")
def welcome_user():
    name = input("please input username")

    return "<h2>Welcome %s </h2>" % name


''' Sohaib's User Name method
@app.route("/<username>")
exercise - create a function called welcome_user
create a decorator to link the page /user
return "welcome to Python flask app dear (user)
def welcome_user(username):
return f"<h1>Welcome to Python flask app dear {username} </h1>"
This is an example of how an argument could be passed through welcome user
'''

if __name__ == "__main__":
    app.run(debug=True)

# print(index())
