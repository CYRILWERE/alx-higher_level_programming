-- 9. List all cities with their corresponding states

USE hbtn_0d_usa;

-- Selecting cities with their corresponding states using JOIN
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;

