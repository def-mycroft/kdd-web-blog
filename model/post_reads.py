from flask import request, session
from model import db_connection, db_helpers
import markdown
import time


def fetch_a_specific_post(post_id, edit_mode=False):
    """Fetches a particular post given a post_id"""
    conn, cur = db_helpers.create_connection()
    cur.execute(
        """
        SELECT * FROM post WHERE id=?
        """, (post_id,)
    )
    data = rows_to_dicts(cur.fetchall())[0]

    data['logged_in'] = session['logged_in']

    # Set edit flag
    if session['user_id'] == data['author_id'] and data['logged_in']:
        data['can_edit'] = True
    else:
        data['can_edit'] = False

    if not edit_mode:
        data['content'] = markdown.markdown(data['content'])
        # TODO write function to convert dates and use it here.

    return data


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
