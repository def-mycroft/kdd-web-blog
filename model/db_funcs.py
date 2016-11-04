import db_connection

conn = db_connection.database_connection()
cur = conn.cursor()

cur.execute('select * from post')
data = cur.fetchall()

print('here is the data')
print(data)


def rows_to_dicts(rows):
    # [Row, Row, Row]
    # row.keys()

    dicts = []
    for row in rows:

        dicts.append(
            dict(map(
                lambda key, value: (key, value),
                row.keys(), row
            )
        ))

    return dicts

print(rows_to_dicts(data))



