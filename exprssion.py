from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)
#link our python file to chinook db with create_engine
db = create_engine("postgresql://postgres:soor1993@localhost/chinook")

# metadata to collect tables and assosiate contents
meta = MetaData(db)
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

album_table = Table(
    "Album",meta,
    Column("AlbumId",Integer,primary_key = True),
    Column("Title",String),
    Column("ArtistId",Integer,ForeignKey("artist_table.ArtistId"))
)

track_table = Table(
    "Track",meta,
    Column("TrackId",Integer,primary_key = True),
    Column("Name",String),
    Column("AlbumId",Integer,ForeignKey("album_tabel.AlbumId")),
    Column("MediaTypeId",Integer,primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer",String),
    Column("Milliseconds",Integer),
    Column("Bytes",Integer),
    Column("UnitPrice",Float),
)

#making the connection
with db.connect() as connection:

    # select all records from "Artist " TABLE
    #select_query = artist_table.select()
    # - select only name column from artist table
    #select_query = artist_table.select().with_only_columns([artist_table.c.Name])
    # - select 'Queen' form Artist table
    #select_query = artist_table.select().where(artist_table.c.Name == "Queen")
    # - select only Artist id of 51 in artist table
    #select_query = artist_table.select().where(artist_table.c.ArtistId == 51)
    # - select only queen albums by habe 51 number
     #select_query = album_table.select().where(album_table.c.ArtistId==51)
    # - select tracks from queen in track table
    select_query = track_table.select().where(track_table.c.Composer == "Queen")



   
    results  = connection.execute(select_query)
    for result in results :
        print(result)




