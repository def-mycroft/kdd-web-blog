from model import db_connection
from flask import request


def create_connection():
    """Creates a conn and cur for db connection"""
    conn = db_connection.database_connection()
    cur = conn.cursor()
    return conn, cur


def get_title_and_content():
    """Pulls the title and content for new and edit posts"""
    title = request.form['post-title']
    content = request.form['post-content']
    return title, content
