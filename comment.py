from flask import Blueprint, render_template, redirect, request
from model import session_db


comment = Blueprint('comment', __name__)


@comment.route('/commit/<post_id>', methods=['POST'], strict_slashes=False)
def commit_comment(post_id):
    """Commits a new comment to database"""
    print('Hello from comment commit')
    return "this is technically html"
