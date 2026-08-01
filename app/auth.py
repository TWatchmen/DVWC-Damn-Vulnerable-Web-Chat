from flask import Blueprint, render_template, request, redirect, url_for, session

from app import database

#%% Authentification routes


auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["GET", "POST"])
def register():
    error = None

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        color = request.form["colors"]

        success = database.register_db(username, password, color)
        if not success:
            error = "Username already exists"
            return render_template("register.html", error=error)

        return redirect(url_for("main.index"))

    return render_template("register.html", error=error)


@auth.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = database.login_db(username, password)

        if user:
            session["username"] = username
            return redirect(url_for("main.index"))

        error = "Login fehlgeschlagen"

    return render_template("login.html", error=error)