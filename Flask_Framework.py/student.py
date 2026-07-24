from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/calculator", methods=["GET", "POST"])
def student():

    if request.method == "POST":

        name = request.form["name"]
        marks = int(request.form["marks"])

        if marks >= 90:
            grade = "A+"
        elif marks >= 80:
            grade = "A"
        elif marks >= 70:
            grade = "B"
        elif marks >= 55:
            grade = "C"
        else:
            grade = "F"

        return render_template(
            "student.html",
            name=name,
            marks=marks,
            grade=grade
        )

    return render_template("form2.html")


if __name__ == "__main__":
    app.run(debug=True)