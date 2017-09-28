from testflaskbower import app
from flask import render_template

@app.route("/")
def index_b():
    return render_template("bowertest.html")
    




