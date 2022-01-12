# loading Flask application for the web application
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    """View function for Home Page."""
    return render_template("home.html")


@app.route("/about")
def about():
    """View function for About Page."""
    return render_template("about.html")



