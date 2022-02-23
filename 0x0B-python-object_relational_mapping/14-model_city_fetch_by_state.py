#!/usr/bin/python3
"""Prints all rows in the cities table
"""
if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker, Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost\
        /{}'.format(sys.argv[1], sys.argv[2],
                    sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker()
    local_session = Session(bind=engine)

    for city, state in local_session.\
            query(City, State).filter(City.state_id == State.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
