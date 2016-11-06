from flask import request
from model import db_helpers, db_connection, session_db

def commit_user():
    """Commits a new user to the database"""
    conn, cur = db_helpers.create_connection()

    username = request.form['username']
    password = request.form['password']
    first_name = request.form['last-name']
    last_name = request.form['last-name']
    email = request.form['user-email']

    cur.execute(
        """
        INSERT INTO user (username, password, first_name, last_name, email)
        VALUES (?, ?, ?, ?, ?)
        """, (username, password, first_name, last_name, email)
    )
    conn.commit()

    session_db.create_session(cur.lastrowid)




