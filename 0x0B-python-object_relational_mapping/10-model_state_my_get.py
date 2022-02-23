#!/usr/bin/python3
"""Lists all states containing the letter 'a'
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, Session

engine = create_engine('mysql+mysqldb://{}:{}@localhost\
    /{}'.format(sys.argv[1], sys.argv[2],
                sys.argv[3]), pool_pre_ping=True)
Base.metadata.create_all(engine)

Session = sessionmaker()
local_session = Session(bind=engine)

states = local_session.query(State).filter(State.name.contains(sys.argv[4]))

count = states.count()

if count > 0:
    print("{}".format(states[0].id))
else:
    print("Not found")
