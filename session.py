from flask import Blueprint, render_template, redirect, request
from model import session_db


session = Blueprint('session', __name__)


@session.route('/login', methods=['GET'], strict_slashes=False)
def render_login():
    """Renders login page for user"""
    return render_template('login.html')


@session.route('/verify', methods=['POST'], strict_slashes=False)
def verify_login():
    """Checks login data"""
    success = session_db.verify_login()
    # TODO display an error message on login screen if login is faulty.
    if success:
        return redirect('/')
    else:
        return redirect('session/login')


@session.route('/logout', methods=['POST', 'GET'], strict_slashes=False)
def logout():
    """Logs out a user"""
    return render_template('logout.html')
