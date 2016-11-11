from flask import request, session
from model import db_connection, db_helpers
import markdown
import time


def fetch_post_comments(post_id):
    """Fetches a dict of comments for a post"""
    # TODO May be able to use a join here, doing it the wrong way for now
    conn, cur = db_helpers.create_connection()
    cur.execute(
        """
        SELECT * FROM comment WHERE post_id=?
        """, (post_id,)
    )

    # TODO comment post dates need dto be convered into human readable form.

    return cur.fetchall()


def fetch_post_content(post_id, edit_mode=False):
    """Fetches a particular post given a post_id"""
    conn, cur = db_helpers.create_connection()
    cur.execute(
        """
        SELECT * FROM post WHERE id=?
        """, (post_id,)
    )
    data = rows_to_dicts(cur.fetchall())[0]

    try:
        data['logged_in'] = session['logged_in']
    except KeyError:
        data['logged_in'] = False
        session['user_id'] = 0

    # Set edit flag
    if session['user_id'] == data['author_id'] and data['logged_in']:
        data['can_edit'] = True
    else:
        data['can_edit'] = False

    if not edit_mode:
        data['content'] = markdown.markdown(data['content'])
        # TODO write function to convert dates and use it here.

    return data


def fetch_a_specific_post(post_id, edit_mode=False):
    """Fetches post content and comments for a post"""

    data = fetch_post_content(post_id, edit_mode)
    comments = fetch_post_comments(post_id)

    return data, comments


def fetch_index_posts():
    """Fetches post data from index page"""
    conn, cur = db_helpers.create_connection()
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
