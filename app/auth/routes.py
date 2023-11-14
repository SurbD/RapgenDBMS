from flask import flash, redirect, render_template, url_for, session, request
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user, login_required

from app.models import User

from . import auth
from .forms import LoginForm, RegisterationForm


@auth.route("/login", methods=["GET", "POST"])
def login():
    # form validation will be done in the frontend later stop page refresh on submit
    form = LoginForm()

    if form.validate_on_submit():
        print("In validate on submit")
        user = User.query.filter_by(email=form.email.data).first()

        # if user and check_password_hash(user.password, form.password.data):
        if user and form.password.data == user.password:
            login_user(user, remember=True)
            next_page = request.args.get('next') # when login_required redirects to login
            if next_page == '/logout':
                next_page = None

            session['email'] = None
            flash('Logged In successfully!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))

        flash('Invalid login information. Please check email or password and try again.', 'danger')
        session['email'] = form.email.data
        return redirect(url_for('auth.login'))

    if request.method == "GET":
        email = session.get('email')
        if email:
            form.email.data = email

    return render_template("auth/login.html", form=form)


@auth.route("/register", methods=["GET", "POST"])
def register():
    """This would be used only once there can only be one user, would be disabled later"""
    form = RegisterationForm

    if form.validate_on_submit():
        pass

    return render_template("auth/register.html")

@auth.route("/reset-password", methods=["GET", "POST"])
def reset_password():
    return "Form for resetting password: Requires email and uses Axios to \
            send the request to send a verification code to the email of exists"

@auth.route("/logout", methods=["POST", "GET"])
@login_required
def logout():
    logout_user()
    flash("Logged Out!, we'll be expecting you soon")
    return redirect(url_for('auth.login'))
