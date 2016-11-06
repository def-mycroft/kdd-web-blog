from flask import request
from model import db_helpers, db_connection

def verify_login():
    """Returns True if valid login"""
    conn, cur = db_helpers.create_connection()

    username = request.form['username']
    password_given = request.form['password']

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



