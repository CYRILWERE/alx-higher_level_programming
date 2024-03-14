#!/usr/bin/python3
"""Changes the name of a State object with id = 2 to New Mexico
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL username, password, and database name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create engine to connect to MySQL server running on localhost at port 3306
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        mysql_username, mysql_password, database_name), pool_pre_ping=True)

    # Create session maker
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query the State object with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    # If state_to_update exists, update its name to "New Mexico"
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close session
    session.close()

