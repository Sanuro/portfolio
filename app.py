from flask import Flask
from flask import render_template
import sched, time
s = sched.scheduler(time.time, time.sleep)
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("portfolio.html")

@app.route("/rokuKeyboard")
def rokuKeyboard():
    return render_template("rokuKeyboard.html")

@app.route("/dogFetchr")
def dogFetchr():
    return render_template("dogFetchr.html")

@app.route("/libraryRedesign")
def library():
    return render_template("libraryRedesign.html")

@app.route("/escapeRoom")
def escapeRoom():
    return render_template("escapeRoom.html")

@app.route("/magazine")
def magazine():
    return render_template("magazine.html")

@app.route("/leadership")
def leadership():
    return render_template("leadership.html")