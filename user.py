from flask import Blueprint, render_template, redirect, request
from model import user_db_edits


user = Blueprint('user', __name__)


@user.route('/signup', methods=['GET'], strict_slashes=False)
def render_signup():
    """Renders signup page for new user"""
    return render_template('new_user.html')


@user.route('/', methods=['POST'], strict_slashes=False)
def create_user():
    """Creates a new user"""
    # TODO need to create a new session after the user is created.
    user_db_edits.commit_user()
    print('hello from create_user')

    # TODO want to create a landing page for a new user.
    return redirect('/')


