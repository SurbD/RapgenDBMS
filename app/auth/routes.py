from flask import render_template, url_for

from . import auth
from .forms import LoginForm


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        print("In validate on submit")
        admin = None # Query the database

    return render_template("login.html", form=form)


@auth.route("/register", methods=["GET", "POST"])
def register():
    """This would be used only once there can only be one user, would be disabled later"""

    return render_template("register.html")

@auth.route("/reset-password", methods=["GET", "POST"])
def reset_password():
    return "Form for resetting password: Requires email and uses Axios to \
            send the request to send a verification code to the email of exists"
