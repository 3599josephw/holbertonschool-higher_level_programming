#!/usr/bin/python3
"""Lists all states containing the letter 'a'
"""

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy import *
    from sqlalchemy.orm import sessionmaker, Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306\
        /{}'.format(sys.argv[1], sys.argv[2],
                    sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new = State(name='Louisiana')

    session.add(new)
    session.commit()

    print("{}".format(new.id))
