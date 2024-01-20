
import psycopg2

# Establish a connection to the database
connection = psycopg2.connect(
    host="localhost",  # Replace with your database server hostname if different
    dbname="chinook",
    password="soor1993",  # Replace with your database password
    user="postgres",
    port=5432
)


# Create a cursor object to execute queries
cursor = connection.cursor()

try:
    #cursor.execute('SELECT * FROM "Album";')  
    #cursor.execute('SELECT "Title" FROM "Album";')
    #cursor.execute('SELECT "Name" FROM "Artist";')

    #if you want to get specific name data you need use place holder
    #cursor.execute('SELECT * FROM "Artist" WHERE "Name" =%s' ,["Queen"])
    #cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s',[51])
    #cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s',[51])
    aname = "Queen"
    cursor.execute('SELECT * FROM "Track" WHERE "Composer"= %s',[aname])

    results = cursor.fetchall()
    #result = cursor.fetchone()
    
    for row in results:
        print(row)
    
except psycopg2.Error as e:
    print("Error:", e)

# Close the cursor and connection
cursor.close()
connection.close()
