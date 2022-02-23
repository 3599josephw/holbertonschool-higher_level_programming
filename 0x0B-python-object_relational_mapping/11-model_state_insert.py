#!/usr/bin/python3
"""Lists all states containing the letter 'a'
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, Session

engine = create_engine('mysql+mysqldb://{}:{}@localhost\
    /{}'.format(sys.argv[1], sys.argv[2],
                sys.argv[3]), pool_pre_ping=True)
Base.metadata.create_all(engine)

Session = sessionmaker()
local_session = Session(bind=engine)

new = State(name='Louisiana')

local_session.add(new)
local_session.commit()

states = local_session.query(State).filter(State.name.contains("Louisiana"))

print("{}".format(states[0].id))
