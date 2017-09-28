from testflaskbower import app
from flask import render_template

@app.route("/teststatic")
def index_a():
    return render_template("statictest.html")

# two routes given for convenience
@app.route("/")
@app.route("/testbower")
def index_b():
    return render_template("bowertest.html")
    




