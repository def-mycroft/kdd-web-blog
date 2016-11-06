from flask import request, session
from model import db_helpers, db_connection


def logout():
    """Logs out user"""
    session['logged_in'] = False


def get_user_and_password():
    """Gets username and password from login form"""
    username = request.form['username']
    password_given = request.form['password']
    return username, password_given


def create_session(user_id):
    """Creates a flask session"""
    username, password_given = get_user_and_password()
    session['username'] = username
    session['user_id'] = user_id
    session['logged_in'] = True


def verify_login():
    """If password matches, create session and return True"""
    conn, cur = db_helpers.create_connection()
    username, password_given = get_user_and_password()

    cur.execute(
        """
        SELECT password, id FROM user WHERE username=?
        """, (username,)
    )

    data = cur.fetchall()

    if len(data) != 0:
        password_actual = data[0][0]

    if password_actual == password_given:
        create_session(data[0][1])
        return True
    else:
        return False
