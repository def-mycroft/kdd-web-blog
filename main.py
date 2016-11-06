from flask import Flask, render_template, redirect, session
from post import post
from user import user
from session_handler import session_handler

app = Flask(__name__)
app.secret_key = "topsecret"


app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(session_handler, url_prefix='/session')
app.register_blueprint(post, url_prefix='/post')


@app.route('/', strict_slashes=False, methods=['GET'])
def index():
    """Renders the main index page"""
    # TODO could remove session data printout, this is for testing
    try:
        print('#' * 80)
        print('Session Data:')
        print('username: %s' % session['username'])
        print('user_id: %s' % session['user_id'])
        print('logged_in: %s' % session['logged_in'])
        print('#' * 80)
    except KeyError:
        print('no session data')
        
    return redirect('/post')


if __name__ == '__main__':
    app.run()
