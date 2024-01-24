from sqlalchemy import (
    create_engine, Column, Float, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session


db = create_engine("postgresql://postgres:soor1993@localhost/chinook")
base = declarative_base()

class Country(base):
    __tablename__ = "Country"
    country_id = Column(Integer,primary_key = True)
    capital =Column(String)
    population = Column(Integer)
    leader = Column(String)
    independence = Column(String)
Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

Portugal = Country(
    capital = "Lisbon",
    population = 10000000,
    independence = "october of 1910",
    leader = "Leon"
    )

Germany = Country(
    capital = "Berlin",
    population = 84000000,
    independence = "october of 1990",
    leader = "Merkel"
    )
session.add(Germany)
session.commit()

rec = session.query(Country)
for r in rec :
    print(r.capital,r.independence,sep="||")