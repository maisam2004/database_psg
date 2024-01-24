from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session


# executing the instructions from the "chinook" database
db = create_engine("postgresql://postgres:soor1993@localhost/chinook")
base = declarative_base()


# create a class-based model for the "Artist" table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


# create a class-based model for the "Album" table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


# create a class-based model for the "Track" table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# Query 1 - select all records from the "Artist" table
""" try:
    albums = session.query(Album).filter_by(ArtistId=51)
    artists = session.query(Artist)
    for artist in artists:
        print(artist.ArtistId,artist.Name, sep=" | ")
except Exception as e:
    print(e)  """
# Query 2 = select only the "Name" column from "Artist" table
    
""" try:
    artists = session.query(Artist)
    for ar in artists:
        print(ar.Name,'--' ,sep="% %")

except Exception as e:
    print(e)
 """
# Query 3 = select only "Queen" from the Aartist table
try:
    artist = session.query(Artist).filter_by(Name = 'Queen').first()
    print(artist.ArtistId,artist.Name)
       
except Exception as e:
    print(e)

# Query 5 = select only album filtered by artist id of 51
""" try:
    albums = session.query(Album).filter_by(ArtistId=51)
    
    for al in albums:
        if len(al.Title) < 17 :
            print(al.ArtistId,al.Title, sep=" | ")
except Exception as e:
    print(e) """

#Query 6 = selcet track that have composer of Queen
try:
    tracks = session.query(Track).filter_by(Composer = "Queen")
    print('TrackId','Name','Album Id ','Composer','Bytes','Unit price',sep='|')
    for tr in tracks :
        print(tr.TrackId,tr.Name,tr.AlbumId,tr.Composer,tr.Bytes,tr.UnitPrice,sep='|')
except Exception as e:
    print(e)