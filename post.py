from flask import Blueprint, render_template
from model import db_funcs, db_connection

post = Blueprint('post', __name__)


@post.route('/<int:post_id>', methods=['get'], strict_slashes=False)
def show_or_update_post(post_id):
    """Shows an individual post"""
    post = db_funcs.fetch_a_specific_post(post_id)
    print(post)
    return render_template('post.html', 
                           post_title=post['title'], 
                           post_author_id=post['author_id'], 
                           post_date_created=post['date_created'], 
                           post_content=post['content'])


@post.route('/new', methods=['GET'], strict_slashes=False)
def new_post():
    """Renders form for new post"""
    return render_template('new_or_update_post.html')


@post.route('/', methods=['GET'], strict_slashes=False)
def show_index():
    """Shows the index page"""
    posts = db_funcs.fetch_index_posts()
    return render_template('index.html', posts=posts)


@post.route('/<int:post_id>/edit', methods=['GET'], strict_slashes=False)
def edit_post(post_id):
    """Returns the edit form with post content"""
    # TODO write function that pulls data from the database and inserts into edit form.
    # Will need to get data from the database and insert into htmlform 
    return render_template('new_or_update_post.html')


@post.route('/', methods=['POST'], strict_slashes=False)
def commit_post(post_id):
    """Commits a new post to the database"""
    # TODO Write a db_Funcs method thae takes post data and commits to database
    return redirect('/<int:post_id>')


# I just have this disabled for now because it is throwing error, probably because of ussie with post_id
# @post.route('/<id:post_id>', methods=['POST'], strict_slashes=False)
# def commit_post_edits(post_id):
#     """Commits post edits to database"""
#     # Take data from html form and update the database accordingly
#     #return redirect('/<int:post_id>')
#     # TODO Afer editing post, should show post and not return to homepage.
#     # going back home for now, want to return to the post after getting databse set up.
#     return render_tempate('index.html') # go




