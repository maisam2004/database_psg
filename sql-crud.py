from sqlalchemy import (
    create_engine, Column, Float, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session


db = create_engine("postgresql://postgres:soor1993@localhost/chinook")
base = declarative_base()

class Programmer1(base):
    __tablename__ = "Programmer"
    id = Column(Integer,primary_key = True)
    frist_name  = Column(String)
    last_name   = Column(String)
    gender      = Column(String)
    nationality = Column(String)
    famous_for  = Column(String)



Session = sessionmaker(db)
session = Session()
base.metadata.create_all(db)

alan_turing = Programmer1( 
    frist_name = "Alan",
    last_name="Turing",
    gender ='M',
    nationality =  "British",
    famous_for ="Modern Computing"
)
grace_hopper = Programmer1( 
    frist_name = "Grace",
    last_name="Hopper",
    gender ='F',
    nationality =  "American",
    famous_for ="COBOL language"
)
margaret_hamilton = Programmer1( 
    frist_name = "Margaret",
    last_name="Hamilton",
    gender ='F',
    nationality =  "American",
    famous_for ="Apolo 11"
)
bill_gates = Programmer1(
    frist_name = "Bill",
    last_name="Gates",
    gender ='M',
    nationality =  "American",
    famous_for ="Microsoft"
)
sam_husei = Programmer1(
    frist_name = "Sam",
    last_name="Hussei",
    gender ='M',
    nationality =  "British",
    famous_for ="code Inst student"
)
#session.add(sam_husei)

#session.commit()


""" mer  = session.query(Programmer1)
for p in mer :
    print(p.frist_name,p.last_name,p.gender,p.nationality) """

""" programmer = session.query(Programmer1).filter_by(id = 7).first()
programmer.famous_for = "World President" """


#session.commit()
#print(programmer.frist_name,programmer.last_name,programmer.famous_for)

""" people = session.query(Programmer1)
for person in people:
    person.gender = "Female" if person.gender == "F" else "Male"
    session.commit() """

#write query to ask for first ans last names then read it in 
#query session , create if it is exist then promt user delet 
#then use session delet and then commit
fname = input('please enter first name')
lname = input('please enater last name')
print(fname)
print(lname)

porgramer_name = session.query(Programmer1).filter_by(frist_name= fname.capitalize(),last_name=lname.capitalize()).first()

if porgramer_name is not None:
    print(
        f"{porgramer_name.id}|{porgramer_name.frist_name} {porgramer_name.last_name}"
    )
    confirmation = input(f'do really want to delet {porgramer_name} record ?(y/n)')
    if confirmation.lower() == 'y':
        session.delete(porgramer_name)
        session.commit()
        print("programer delete successfully")
    else:
        print("not worry not deleted")
else:
    print("No one has been found")
    to_see = session.query(Programmer1)
    for i in to_see:
        print(i.id,i.last_name,sep="||")

