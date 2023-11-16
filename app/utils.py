from flask import current_app, render_template
from flask_mail import Message
from threading import Thread

from app import mail


def send_async_mail(app, msg):
    with app.app_context():
        mail.send(msg)

def send_mail(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    message = Message(current_app.config["RAPGENDBMS_MAIL_SUBJECT_PREFIX"] + subject,
                      sender=current_app.config['RAPGENDBMS_MAIL_SENDER'], recipients=[to])
    message.body = render_template(template + '.txt', **kwargs)
    message.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_mail, args=[app, message])
    thr.start()
    return thr
