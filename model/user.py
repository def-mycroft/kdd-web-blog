from flask import Blueprint, render_template, redirect, request
from model import user_db
from model import session_db


user = Blueprint('user', __name__)


@user.route('/signup', methods=['GET'], strict_slashes=False)
def render_signup():
    """Renders signup page for new user"""
    return render_template('new_user.html')


@user.route('/', methods=['POST'], strict_slashes=False)
def create_user():
    """Creates a new user and creates a session for new user"""
    user_db.commit_user() # Session is created in user_db
    return redirect('/')


