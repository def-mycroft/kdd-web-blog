from model import db_connection

conn = db_connection.database_connection()
cur = conn.cursor()

cur.execute('select * from post')
data = cur.fetchall()

print(data)
print(db_connection.convert_to_dict(data))

