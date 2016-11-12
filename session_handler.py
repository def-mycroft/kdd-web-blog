from flask import Blueprint, render_template, redirect, request
from model import session_db


session_handler = Blueprint('session', __name__)


@session_handler.route('/login', methods=['GET'], strict_slashes=False)
def render_login():
    """Renders login page for user"""
    return render_template('login.html')


@session_handler.route('/verify', methods=['POST'], strict_slashes=False)
def verify_login():
    """Checks login data"""
    success = session_db.verify_login()
    if success:
        return redirect('/')
    else:
        return redirect('session_handler/login')


@session_handler.route('/logout', methods=['POST', 'GET'], strict_slashes=False)
def logout():
    """Logs out a user"""
    session_db.logout()
    return render_template('logout.html')
