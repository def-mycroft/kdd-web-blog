from flask import Blueprint, render_template

post = Blueprint('post', __name__)

@post.route('/', strict_slashes=False)
def show_index():
    """Shows the index page"""
    return render_template('index.html')

@post.route('/<int:post_id>', methods=['GET', 'POST'], strict_slashes=False)
def show_or_update_post(post_id):
    if request.method == 'POST':
        return render_template('post.html')
