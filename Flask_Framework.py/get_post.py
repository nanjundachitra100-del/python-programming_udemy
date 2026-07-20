from flask import Flask , render_template

app=Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to the page!"

@app.route("/index")
def object():
    return render_template("index.html")







if __name__ == "__main__":
    app.run(debug=True)

