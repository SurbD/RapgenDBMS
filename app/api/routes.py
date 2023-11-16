from flask import request, redirect, session
from flask_login import current_user

from . import api, db

@api.route('/confirm_verification_code', methods=["POST"])
def confirm_verification_code():
    if current_user.confirmed:
        return redirect(url_for('main.home'))

    token = session.get('verification_code_token')
    code = request.get_json().get('verification_code')

    user = current_user.confirm_code(token, code)

    if user:
        user.confirmed = True
        db.session.commit()
        
        flash('Your account has been verified!', 'success')
        return redirect(url_for('main.home'))
    else:
        return {'response': 'Invalid verification code. Try again or request for a new code'}
