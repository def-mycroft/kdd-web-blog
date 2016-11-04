from flask import Blueprint, render_template, redirect, request

user = Blueprint('user', __name__)

@user.route('/signup', methods=['GET'], strict_slashes=False)
def render_signup():
    """Renders signup page for new user"""
    return render_template('new_user.html')


@user.route('/', methods=['POST'], strict_slashes=False)
def create_user():
    """Creates a new user"""
    # Will have to post this to the database to create a new user.
    # will also probably wnat to create a new session so that the user is active.
    # TODO commit users to database.
    print(
        request.form['username'],
        request.form['password']
    )

    # TODO want to create a landing page for a new user.
    return render_template('index.html')


