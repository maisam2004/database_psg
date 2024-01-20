import psycopg2

conn = psycopg2.connect(
    host="localhost",  # Replace with your database server hostname if different
    dbname="chinook",
    password="soor1993",  # Replace with your database password
    user="postgres",
    port=5432
)
cursor = conn.cursor()


#cursor.execute('SELECT * FROM "Artist"')
#cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s',["Body Guy"])
#cursor.execute('SELECT * FROM "Track" WHERE "Composer"= %s',["Nando Reis"])
cursor.execute('SELECT * FROM "Track" WHERE "Composer"= %s',["test"])
results = cursor.fetchall()

if len(results) != 0:
    for r in results:
        print(r)
else:
    print('no results')


cursor.close()
conn.close()