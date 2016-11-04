import sqlite3
import os


def test_function():
    print('hello from the database connection module.')


def database_connection():
    """Creates a database connection. Creates a new database using init_db"""

    database_exists = os.path.isfile('database.db')
    db_conn = sqlite3.connect('database.db')

    if not database_exists:
        create_database(db_conn)

    # TODO I don't know what this rowfactor thing does. May want to start usin
    # this and do some researcjj
    db_conn.row_factory = sqlite3.Row

    return db_conn


def create_database(db_conn):
    """Initializes a new database"""

    cur = db_conn.cursor()

    # Create user table.
    cur.execute(
        """
        CREATE TABLE user(
            id integer primary key,
            username text unique not null,
            password text not null,
            first_name text,
            last_name text,
            email text
        )
        """
    )

    # Create post table.
    cur.execute(
        """
        CREATE TABLE post(
            id integer primary key,
            title text not null,
            content text,
            date_created integer,
            author_id integer references user(id)
        )
        """
    )
    # TODO Create comments table.

    # Create admin user.

    cur.execute(
        """
        INSERT INTO user
            (username, password) values ('admin', 'password')
        """
    )

    db_conn.commit()


def convert_to_dict(input_object):
    """Converts a single row object from database into a dictionary"""

    dict = []

    for row in input_object:
        dict.append(
            dict(map(
                lambda key, value: (key, value),
                row.keys(), row
                )
            )
        )


    return dict





