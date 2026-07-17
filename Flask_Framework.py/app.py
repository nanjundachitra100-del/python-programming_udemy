from flask import Flask

#creating an instance of the flask framework

#WSGI application
app=Flask(__name__)

@app.route("/")#home page
def welcome():
    return "welcome to this class.This should be great"

@app.route("/index")
def index():
    return "welcome dear!"


if __name__ == "__main__":   #from here only the execution of the app strarts
    app.run(debug=True)
  





