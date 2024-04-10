-- 8. List all cities of California

USE hbtn_0d_usa;

-- Using subquery to find the state_id for California
SELECT * FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;

