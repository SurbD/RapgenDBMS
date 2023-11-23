from flask import flash, redirect, render_template, url_for, session, request
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user, login_required, current_user

from app.models import User, db
from app.utils import send_mail

from . import auth
from .forms import LoginForm, RegisterationForm, VerificationForm


@auth.before_app_request
def before_request():
    if current_user.is_authenticated and not current_user.confirmed \
        and request.blueprint != 'auth' and request.endpoint != 'static':
        return redirect(url_for('auth.unconfirmed'))

@auth.route("/unconfirmed")
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.home'))
    return render_template('auth/unconfirmed.html')


@auth.route("/login", methods=["GET", "POST"])
def login():
    # form validation will be done in the frontend later stop page refresh on submit
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = LoginForm()

    if form.validate_on_submit():
        print("In validate on submit")
        user = User.query.filter_by(email=form.email.data).first()

        # if user and form.password.data == user.password:
        if user and check_password_hash(user.password, form.password.data):
            # TODO: set remember state to 1day
            login_user(user, remember=True)
            next_page = request.args.get('next') # when login_required redirects to login
            if next_page == '/logout':
                next_page = None

            session['email'] = None
            # flash('Logged In successfully!', 'success')
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
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegisterationForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(username=form.username.data,
                    email=form.email.data.lower(), password=hashed_password)

        db.session.add(user)
        db.session.commit()
        flash("Your account has been created successfully!!. You can now login.", "success")
        return redirect(url_for('auth.login')) # Change to redirect to verification template

    return render_template("auth/register.html", form=form)

@auth.route("/logout", methods=["POST", "GET"])
@login_required
def logout():
    if request.method == 'POST':
        logout_user()
        flash("Logged Out!, we'll be expecting you soon", "info")
        return redirect(url_for('auth.login'))
    return render_template("auth/logout.html")

@auth.route("/confirm-verification", methods=["GET", "POST"])
@login_required
def confirm_verification():
    if current_user.confirmed:
        return redirect(url_for("main.home"))

    form = VerificationForm()

    if form.validate_on_submit():
        print('invalidate')
        token = session.get('verification_token')
        user = User.confirm_code(token, form.code.data)
        if user:
            user.confirmed = True
            db.session.commit()
            session.pop('verification_token')
            flash("You're account has been verified!. You can now login.", "success")
            return redirect(url_for('auth.login'))

        print('not confirmed')
        flash("Invalid verification code. please try again or request for another code", "danger")
    print('emd of form')
    return render_template("auth/verify_account.html", form=form)

@auth.route("/verify-account")
@login_required
def verify_account():
    if current_user.confirmed:
        return redirect(url_for('main.home'))
    token, code = current_user.get_verification_code().values()

    send_mail(
        to=current_user.email,
        subject="Verify your RapgenDBMS account",
        template="email/verify_account",
        username=current_user.username, code=code
    )

    session['verification_token'] = token
    flash("The verification code has been sent to your email", "success")
    return redirect(url_for("auth.confirm_verification"))

@auth.route("/reset-password")
def reset_password():
    """Nothing here for now"""

    return {}
