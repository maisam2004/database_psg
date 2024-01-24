from sqlalchemy import (
    create_engine, Column, Float, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session

db = create_engine("postgresql://postgres:soor1993@localhost/chinook")
base = declarative_base()

class Mobile(base):
    __tablename__ = "Mobile"
    mobile_id = Column(Integer,primary_key= True)
    brand = Column(String)
    model = Column(String)
    release = Column(String)
    price = Column(Float)

Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)




