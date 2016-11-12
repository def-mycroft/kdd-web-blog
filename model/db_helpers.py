from model import db_connection
from flask import request
import time


def convert_time(time_integer):
    """Creates human readable date / time given seconds since epoch"""

    # Parse input time integer
    time_list = time.gmtime(time_integer)
    mon = time_list[1]
    day = time_list[2]
    year = time_list[0]
    hour = time_list[3]
    minute = time_list[4]

    if minute < 10:
        minute = '0%s' % minute

    time_string = '%s/%s/%s %s:%s' % (mon, day, year, hour, minute)

    return time_string # example: 10/30/2016 1:30


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
