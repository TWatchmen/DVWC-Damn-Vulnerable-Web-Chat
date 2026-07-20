from flask import Blueprint, render_template

vuln = Blueprint("vuln", __name__)

@vuln.route("/")
def index():
    return render_template("index.html")