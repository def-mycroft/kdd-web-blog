from flask import request
from model import db_connection, db_helpers
import markdown
import time


def commit_new_comment(author_id, post_id, content):
    """Commits a new comment to the database"""
    print('hello from commit new comment in model')
    conn, cur = db_helpers.create_connection()
    cur.execute(
        """
        INSERT INTO comment (author_id, post_id, date_created, content)
        VALUES(?, ?, ?, ?)
        """, (author_id, post_id, int(time.time()), content)
    )
    conn.commit()

def commit_post_edits(post_id):
    """Commits post edits to database"""
    conn, cur = db_helpers.create_connection()
    title, content = db_helpers.get_title_and_content()
    cur.execute(
        """
        UPDATE post
        SET title=?, content=?  WHERE id=?
        """, (title, content, post_id)
    )
    conn.commit()


def commit_new_post():
    """Commits a new post to the database"""
    conn, cur = db_helpers.create_connection()
    title, content = db_helpers.get_title_and_content()
    cur.execute(
        """
        INSERT INTO post (title, content, date_created, author_id)
        VALUES(?,?,?,?)
        """, (title, content, int(time.time()), 1)
        # TODO I have the author id set to 1 for testing, will need
        # to pull the actual author id from the session later.
    )
    conn.commit()
    post_id = cur.lastrowid

    return post_id
