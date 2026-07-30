from flask import Blueprint, render_template, request, redirect, url_for

from app import database

#%% Authentification routes


auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["GET", "POST"])
def register():
    error = None

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        success = database.register_db(username, password)
        if not success:
            error = "Username already exists"
            return render_template("register.html", error=error)
        else:
            return redirect(url_for("main.index"))

    return render_template("register.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        success = database.login_db(username, password)

        if not success:
            error = "Wrong username or password"
            return render_template("login.html", error=error)

        return redirect(url_for("main.index"))

    return render_template("login.html", error=error)