from model import db_connection

def fetch_index_posts():
    """Fetches post data from index page"""

    conn = db_connection.database_connection()
    cur = conn.cursor()

    # TODO This is currently displaying the numerical author ID, want to display name instead.
    # Can probably pull this when creatin dictionarl;
    # should be able to join this table with the user table and pull it all at once

    cur.execute(
        """
        SELECT * FROM post
        """
    )

    data = cur.fetchall()

    return rows_to_dicts(data)


def rows_to_dicts(rows):
    """Takes a list of database rows and converts to a dict"""
    return list(map(lambda row: dict(zip(row.keys(), row)), rows))
