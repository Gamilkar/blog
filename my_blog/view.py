from app import app
from flask import render_template


@app.route("/")
def index():
    text = "some text"
    return render_template("index.html", text=text)
