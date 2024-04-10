-- Print full description of table first_table
SELECT CONCAT('Table\tCreate Table') AS "Table Description"
UNION
SELECT table_name, create_statement
FROM (
    SELECT table_name, create_statement
    FROM information_schema.tables
    WHERE table_schema = 'hbtn_0c_0' AND table_name = 'first_table'
) AS tables_info;

