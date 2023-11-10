""" MODULE DOC STRING"""
from flask import render_template, url_for

from . import auth


@auth.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@auth.route("/register", methods=["GET", "POST"])
def register():
    """This would be used only once there can only be one user, would be disabled later"""

    return render_template("register.html")
