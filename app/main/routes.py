from flask import render_template, redirect, url_for
from flask_login import current_user
from . import main

@main.route('/')
def home():
    if current_user.is_authenticated:
        return render_template('index.html')

    # return render_template('landing_page.html')
    return redirect(url_for('auth.register'))
