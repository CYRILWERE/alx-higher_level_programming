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

    # Execute SQL query to select states where name matches the argument provided (using parameterized query)
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all the rows and print them
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()

