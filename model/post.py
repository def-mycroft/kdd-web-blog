from flask import Blueprint, render_template, redirect, session, jsonify, request
from model import db_connection, post_reads, post_updates, db_helpers
import time

post = Blueprint('post', __name__)


@post.route('/', methods=['GET'], strict_slashes=False)
def show_index():
    """Shows the index page"""
    posts = post_reads.fetch_index_posts()
    return render_template('index.html', posts=posts)


@post.route('/<int:post_id>/comment', methods=['POST'], strict_slashes=False)
def new_comment(post_id):
    """Commits a new comment to the database and displays"""
    author_id = session['user_id']
    content = request.form['comment_content']
    post_updates.commit_new_comment(author_id, post_id, content)
    date = int(time.time())

    return render_template(
        'new_comment.html', 
        author_name=session['username'], 
        date_created= db_helpers.convert_time(date), 
        content=content
    )


@post.route('/<int:post_id>', methods=['GET'], strict_slashes=False)
def show_individual_post(post_id):
    """Shows an individual post"""
    post, comments = post_reads.fetch_a_specific_post(post_id)

    return render_template(
        'post.html',
        post = post,
        comments = comments,
        # Includes script in base.html
        optional = """<script src="/static/js/newcomment.js" type="text/javascript" charset="uft-8"></script>"""
    )


@post.route('/new', methods=['GET'], strict_slashes=False)
def new_post():
    """Renders form for new post"""
    return render_template('new_or_update_post.html')


@post.route('/commit-new', methods=['POST'], strict_slashes=False)
def commit_post():
    """Commits a new post to the database"""
    post_id = post_updates.commit_new_post()
    return redirect('post/%s' % post_id)


@post.route('/<int:post_id>/edit', methods=['GET'], strict_slashes=False)
def edit_post(post_id):
    """Renders form for editing a post"""
    post, comments = post_reads.fetch_a_specific_post(post_id, edit_mode=True)

    if post['can_edit']:
        return render_template('new_or_update_post.html', post=post, edit_mode=True)
    else:
        return redirect('/') # Redirects to home page if user cannot edit.


@post.route('/<int:post_id>/delete', methods=['GET'], strict_slashes=False)
def delete_post(post_id):
    """Deletes a post"""
    post_updates.delete_post(post_id)
    return redirect('/')


@post.route('/<int:post_id>/edit/', methods=['POST'], strict_slashes=False)
def commit_post_edits(post_id):
    """Commits edits for a post"""
    post_updates.commit_post_edits(post_id)
    return redirect('post/%s' % post_id)
