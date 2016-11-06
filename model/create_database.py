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

    # Create admin user.
    cur.execute(
        """
        INSERT INTO user
            (username, password) values ('admin', 'password')
        """
    )

    cur.execute(
        """
        CREATE TABLE comment(
        id integer primary key,
        author_id integer references user(id),
        post_id integer references post(id),
        date_created integer,
        content text
        )
        """
    )

    db_conn.commit()
