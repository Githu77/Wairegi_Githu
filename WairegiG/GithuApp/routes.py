from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_mail import Message
from GithuApp import mail

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html', name="Home")

@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        
        msg = Message(subject, sender=email, recipients=['githubenard16@gmail.com'])
        msg.body = f"Email: {email}\n\n{message}"
        mail.send(msg)
        
        flash('Message sent successfully!')
        return redirect(url_for('main.contact'))

    return render_template('index.html')

@main_bp.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
