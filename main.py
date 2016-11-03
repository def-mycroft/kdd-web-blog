from flask import Flask, render_template, redirect
from post import post

app = Flask(__name__)

#app.register_blueprint(user, url_prefix='/user')
#app.register_blueprint(session, url_prefix='/session')
app.register_blueprint(post, url_prefix='/post')

@app.route('/')
def index():
    return redirect('/post')


if __name__ == '__main__':
    app.run()
