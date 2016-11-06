from flask import Blueprint, render_template, redirect 
from model import db_connection, post_reads, post_updates

post = Blueprint('post', __name__)


@post.route('/', methods=['GET'], strict_slashes=False)
def show_index():
    """Shows the index page"""
    posts = post_reads.fetch_index_posts()
    return render_template('index.html', posts=posts)


@post.route('/<int:post_id>', methods=['GET'], strict_slashes=False)
def show_individual_post(post_id):
    """Shows an individual post"""
    post = post_reads.fetch_a_specific_post(post_id)

    return render_template(
        'post.html',
        post_title=post['title'],
        post_author_id=post['author_id'],
        post_date_created=post['date_created'],
        post_content=post['content'],
        edit_mode=False
    )


@post.route('/new', methods=['GET'], strict_slashes=False)
def new_post():
    """Renders form for new post"""
    return render_template('new_or_update_post.html')


@post.route('/commit-new', methods=['POST'], strict_slashes=False)
def commit_post():
    """Commits a new post to the database"""
    # TODO it would be nice to direct toward the newly-created post.
    post_id = post_updates.commit_new_post()
    return redirect('post/%s' % post_id)


@post.route('/<int:post_id>/edit', methods=['GET'], strict_slashes=False)
def edit_post(post_id):
    """Renders form for editing a post"""
    post = post_reads.fetch_a_specific_post(post_id, edit_mode=True)
    return render_template('new_or_update_post.html', post=post, edit_mode=True)


@post.route('/<int:post_id>/edit/', methods=['POST'], strict_slashes=False)
def commit_post_edits(post_id):
    """Commits edits for a post"""
    post_updates.commit_post_edits(post_id)
    return redirect('post/%s' % post_id)
