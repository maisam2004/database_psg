
import psycopg2

# Establish a connection to the database
connection = psycopg2.connect(
    host="localhost",  # Replace with your database server hostname if different
    dbname="chinook",
    password="soor1993",  # Replace with your database password
    user="postgres",
    port=5432
)
print('this is ',connection.dsn)

# Create a cursor object to execute queries
cursor = connection.cursor()

try:
    cursor.execute('SELECT * FROM "Album";')  

    results = cursor.fetchall()
    for row in results:
        print(row)
except psycopg2.Error as e:
    print("Error:", e)

# Close the cursor and connection
cursor.close()
connection.close()
