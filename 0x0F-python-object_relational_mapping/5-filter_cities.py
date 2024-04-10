#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL username, password, database name, and state name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute SQL query to select cities of the given state
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch all the rows and concatenate city names into a comma-separated string
    cities = cursor.fetchall()
    city_names = ", ".join(city[0] for city in cities)

    # Print the comma-separated city names or a message if no cities found
    if city_names:
        print(city_names)
    else:
        print("No cities found for the state:", state_name)

    # Close cursor and database connection
    cursor.close()
    db.close()

