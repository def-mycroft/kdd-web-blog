from flask import request, session
from model import db_connection, db_helpers
import markdown
import time


def fetch_post_comments(post_id):
    """Fetches a dict of comments for a post"""
    conn, cur = db_helpers.create_connection()
    cur.execute(
        """
        SELECT comment.*, user.username FROM comment
        INNER JOIN
        user ON comment.author_id=user.id WHERE comment.post_id=?
        """, (post_id,)
    )

    data = rows_to_dicts(cur.fetchall())

    for row in data:
        row['date_created'] = db_helpers.convert_time(row['date_created'])

    return sorted(data, key = lambda x: x['date_created'], reverse=True)


def fetch_post_content(post_id, edit_mode=False):
    """Fetches a particular post given a post_id"""
    conn, cur = db_helpers.create_connection()
    cur.execute(
        """
        SELECT post.*, user.username FROM post
        INNER JOIN
        user ON post.author_id=user.id WHERE post.id=?
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
        data['date_created'] = db_helpers.convert_time(data['date_created'])

    return data


def fetch_a_specific_post(post_id, edit_mode=False):
    """Fetches post content and comments for a post"""

    data = fetch_post_content(post_id, edit_mode)
    comments = fetch_post_comments(post_id)

    return data, comments


def fetch_index_posts():
    """Fetches post data from index page"""
    conn, cur = db_helpers.create_connection()
    cur.execute(
        """
        SELECT post.*, user.username FROM post
        INNER JOIN
        user ON post.author_id=user.id
        """
    )
    data = rows_to_dicts(cur.fetchall())

    for post in data:
        post['content'] = markdown.markdown(post['content'])
        post['date_created'] = db_helpers.convert_time(post['date_created'])

    return data


def rows_to_dicts(rows):
    """Takes a list of database rows and converts to a dict"""
    return list(map(lambda row: dict(zip(row.keys(), row)), rows))
