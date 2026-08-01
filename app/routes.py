from flask import Blueprint, render_template, session, redirect, url_for
from app import database

#%% General routes

main = Blueprint("main", __name__)

@main.route("/")
def index():
    username = session.get("username")

    if username:
        color = database.get_user_color(username)
    else:
        color = "grey"

    return render_template(
        "index.html",
        username=username,
        color=color
    )


@main.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("main.index"))
