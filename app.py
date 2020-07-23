from flask import Flask, render_template

app = Flask(__name__)

# index page, this is what is first displayed
@app.route("/")
def index():
    return "<h1>Welcome to my Flask project</h1>"

# second page for the application
# # asks for user input from within the terminal
@app.route("/user")
def welcome_user():
    # name = input("please input username")
    #
    # return "<h2>Welcome %s </h2>" % name
    return render_template('user.html')


''' Sohaib's User Name method
@app.route("/<username>")
exercise - create a function called welcome_user
create a decorator to link the page /user
return "welcome to Python flask app dear (user)
def welcome_user(username):
return f"<h1>Welcome to Python flask app dear {username} </h1>"
This is an example of how an argument could be passed through welcome user
'''
# runs the application
if __name__ == "__main__":
    app.run(debug=True)

# print(index())
