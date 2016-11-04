from flask import Blueprint, render_template

post = Blueprint('post', __name__)


# Create CRUD method 
@post.route('/new', methods=['GET'], strict_slashes=False)
def new_post():
    """Renders form for new post"""
    return render_template('new_or_update_post.html')


@post.route('/', methods=['POST'], strict_slashes=False)
def commit_post(post_id):
    """Commits a new post to the database"""
    return redirect('/<int:post_id>')


# Read CRUD method.
@post.route('/', methods=['GET'], strict_slashes=False)
def show_index():
    """Shows the index page"""
    return render_template('index.html')

@post.route('/<int:post_id>', methods=['GET'], strict_slashes=False)
def show_or_update_post(post_id):
    """Shows an individual post"""
    # TODO Will need to use a database method to get hte information from the 
    # individual post, and pass specific values into the post template.
    return render_template('post.html')


@post.route('/<int:post_id>/edit', methods=['GET'], strict_slashes=False)
def edit_post(post_id):
    """Returns the edit form with post content"""
    # Will need to get data from the database and insert into htmlform 
    return render_template('new_or_update_post.html')


# I just have this disabled for now because it is throwing error, probably because of ussie with post_id
# @post.route('/<id:post_id>', methods=['POST'], strict_slashes=False)
# def commit_post_edits(post_id):
#     """Commits post edits to database"""
#     # Take data from html form and update the database accordingly
#     #return redirect('/<int:post_id>')
#     # TODO Afer editing post, should show post and not return to homepage.
#     # going back home for now, want to return to the post after getting databse set up.
#     return render_tempate('index.html') # go




