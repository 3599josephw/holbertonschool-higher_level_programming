#!/usr/bin/python3
"""Lists all states containing the letter 'a'
"""

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker, Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306\
                        /{}'.format(sys.argv[1], sys.argv[2],
                                    sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    local_session = Session()

    for state in local_session.query(State).filter(State.name.contains('a'))\
            .order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    local_session.close()
