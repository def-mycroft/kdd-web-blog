import sqlite3
import os
from model import create_database


def test_function():
    print('hello from the database connection module.')


def database_connection():
    """Creates a database connection. Creates a new database using init_db"""

    database_exists = os.path.isfile('database.db')
    db_conn = sqlite3.connect('database.db')

    if not database_exists:
        create_database.create_database(db_conn)

    # TODO I don't know what this rowfactor thing does. May want to start usin
    # this and do some researcjj
    db_conn.row_factory = sqlite3.Row

    return db_conn
