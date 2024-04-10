-- 6. Create database hbtn_0d_usa and table states

-- Creating database hbtn_0d_usa if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switching to the database hbtn_0d_usa
USE hbtn_0d_usa;

-- Creating table states if not exists
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

