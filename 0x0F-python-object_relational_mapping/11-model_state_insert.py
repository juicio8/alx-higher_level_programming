#!/usr/bin/python3
"""
11-model_state_insert module
"""
import sys
from sqlachemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = session_maker(bind=engine)
    session = Session()

    lousiana = State(name="louisiana")
    session.add(louisiana)
    session.commit()
    print(louisiana.id)
