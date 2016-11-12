from flask import request, session
from model import db_connection, db_helpers
import markdown
import time


def delete_post(post_id):
    """Delete a post"""
    conn, cur = db_helpers.create_connection()
    cur.execute(
        """
        DELETE FROM post WHERE id=?
        """, (post_id,)
    )
    cur.execute(
        """
        DELETE FROM comment WHERE post_id=2
        """
    )
    conn.commit()


def commit_new_comment(author_id, post_id, content):
    """Commits a new comment to the database"""
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
        """, (title, content, int(time.time()), session['user_id'])
    )
    conn.commit()
    post_id = cur.lastrowid

    return post_id
