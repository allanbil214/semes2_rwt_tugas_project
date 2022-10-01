from flask import Flask, redirect, render_template, request, url_for, flash, session
from model import Model

app = Flask(__name__)
app.config["SECRET_KEY"] = "123"
db = Model()

@app.route("/")
def index():
    total = db.getCount()
    total_course = total[0]
    total_event = total[1]
    total_sensei = total[2]
    total_student = total[3]
    return render_template(
        "index.html",
        course = total_course, 
        event = total_event,
        sensei = total_sensei,
        student = total_student)

@app.route("/about")
def about():
    total = db.getCount()
    total_course = total[0]
    total_event = total[1]
    total_sensei = total[2]
    total_student = total[3]
    return render_template(
        "about.html",
        course = total_course, 
        event = total_event,
        sensei = total_sensei,
        student = total_student)

# @app.route("/course")
# def course():
#     courses = db.getcourseprice()
#     aikido = courses[0]
#     judo = courses[1]
#     iaido = courses[2]
#     karate = courses[3]
#     kendo = courses[4]
#     print(kendo)
#     return render_template(
#         "courses.html",
#         aikido = aikido, 
#         judo = judo,
#         iaido = iaido,
#         karate = karate,
#         kendo = kendo)

@app.route("/course")
def course():
    return render_template("courses.html")

@app.route("/sensei")
def sensei():
    return render_template("trainers.html")

@app.route("/event")
def event():
    return render_template("events.html")

@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)