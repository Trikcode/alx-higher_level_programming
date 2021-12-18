#!/usr/bin/python3
""" prints the State object with the name passed as argument
    from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    query = session.query(State).order_by(State.id).filter(
            State.name == sys.argv[4]).all()
    if len(query) == 0:
        print("Not found")

    for numberid in query:
        print("{}".format(numberid.id))
    session.close()
