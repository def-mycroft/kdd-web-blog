from flask import request, session
from model import db_helpers, db_connection


def get_user_and_password():
    """Gets username and password from login form"""
    username = request.form['username']
    password_given = request.form['password']
    return username, password_given


def create_session():
    """Creates a flask session"""
    username, password_given = get_user_and_password()
    session['username'] = username
    session['logged_in'] = True


def verify_login():
    """Returns True if valid login"""
    conn, cur = db_helpers.create_connection()
    username, password_given = get_user_and_password()

    cur.execute(
        """
        SELECT password FROM user WHERE username=?
        """, (username,)
    )

    password_actual = cur.fetchall()

    if len(password_actual) != 0:
        password_actual = password_actual[0][0]

    if password_actual == password_given:
        return True
    else:
        return False
