from flask import Flask ,render_template

#creating an instance of the flask framework

#WSGI application
app=Flask(__name__)

@app.route("/")#home page
def welcome():
    return "welcome to this class.This should be great"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/success/<int:score>")
def success(score):
    res=""
    if score >=55:
        res="Passed"
    else:
        res="Failed"

    return render_template("result.html",result=res)

@app.route("/student")
def student():
    name="Karthik"
    age=18
    village="Yettukodi"
    college="REVA_University"
    return render_template("result.html",name=name,age=age,place=village,college=college)


if __name__ == "__main__":   #from here only the execution of the app strarts
    app.run(debug=True)
  





