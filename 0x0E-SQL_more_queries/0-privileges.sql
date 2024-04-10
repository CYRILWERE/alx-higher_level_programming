-- 0. My privileges!

-- Lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).

-- Creating user user_0d_1 and granting privileges
CREATE USER 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Listing privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Creating user user_0d_2 (if not exists) and granting privileges
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';

-- Listing privileges for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';

