from flask import Flask, render_template, redirect
from post import post
from user import user

app = Flask(__name__)

app.register_blueprint(user, url_prefix='/user')
#app.register_blueprint(session, url_prefix='/session')
app.register_blueprint(post, url_prefix='/post')


@app.route('/', strict_slashes=False, methods=['GET'])
def index():
    """Renders the main index page"""
    return redirect('/post')


if __name__ == '__main__':
    app.run()
