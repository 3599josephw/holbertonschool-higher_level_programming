#!/usr/bin/python3
"""Prints out all state names and ids
"""

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306\
        /{}'.format(sys.argv[1], sys.argv[2],
                    sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    local_session = Session()

    states = local_session.query(State).all()

    for item in states:
        print("{}: {}".format(item.id, item.name))

    local_session.close()
