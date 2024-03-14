#!/usr/bin/python3
"""Creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


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

    # Create California state
    california = State(name="California")

    # Create San Francisco city
    san_francisco = City(name="San Francisco")

    # Add San Francisco city to California state
    california.cities.append(san_francisco)

    # Add California state and San Francisco city to session
    session.add(california)
    session.add(san_francisco)

    # Commit changes
    session.commit()

    # Close session
    session.close()

