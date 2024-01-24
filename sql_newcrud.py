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
"""
base.metadata.drop_all(db)
"""
Samsung = Mobile(
    brand = "samsung",
    model = "fold 5",
    release = "August 23",
    price = 1600.00
    )
Samsungul = Mobile(
    brand = "samsung",
    model = "s24 Ultra",
    release = "january 24",
    price = 1240.00
    )
oneplus = Mobile(
    brand = "Oneplus",
    model = "11 pro",
    release = "january 23",
    price = 840.00
    )
session.add(Samsung)
session.add(Samsungul)
session.add(oneplus)
session.commit()

try:
    moiles = session.query(Mobile)
    for m in moiles:
        print(m.model,m.price,sep="||")
  
            
except Exception as e:
    print(e)


