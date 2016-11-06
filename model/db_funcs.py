from flask import request
from model import db_connection
import markdown
import time


def commit_post_edits(post_id):
    """Commits post edits to database"""

    conn = db_connection.database_connection()
    cur = conn.cursor()

    title = request.form['post-title']
    content = request.form['post-content']

    cur.execute(
        """
        UPDATE post
        SET title=?, content=?  WHERE id=?
        """, (title, content, post_id)
    )

    conn.commit()


def commit_new_post():
    """Commits a new post to the database"""

    conn = db_connection.database_connection()
    cur = conn.cursor()

    title = request.form['post-title']
    content = request.form['post-content']

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

    # TODO I might want to create rudimentary error handline here

    return post_id



def fetch_a_specific_post(post_id, edit_mode=False):
    """Fetches a particular post given a post_id"""

    conn = db_connection.database_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT * FROM post WHERE id=?
        """, (post_id,)
    )

    data = rows_to_dicts(cur.fetchall())[0]

    if not edit_mode:
        data['content'] = markdown.markdown(data['content'])
        # TODO write function to convert dates and use it here.

    return data


def fetch_index_posts():
    """Fetches post data from index page"""
    conn = db_connection.database_connection()
    cur = conn.cursor()

    # TODO This is currently displaying the numerical author ID, want to display name instead.
    # Can probably pull this when creatin dictionarl;
    # should be able to join this table with the user table and pull it all at once

    cur.execute(
        """
        SELECT * FROM post
        """
    )

    data = rows_to_dicts(cur.fetchall())

    for post in data:
        post['content'] = markdown.markdown(post['content'])
        # TODO write function to convert dates and use it here.

    return data


def rows_to_dicts(rows):
    """Takes a list of database rows and converts to a dict"""
    return list(map(lambda row: dict(zip(row.keys(), row)), rows))
