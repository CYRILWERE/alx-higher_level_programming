-- 5. Create table unique_id

USE hbtn_0d_2;

-- Creating table unique_id if not exists
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

