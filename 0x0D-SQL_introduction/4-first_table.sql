-- Creates a table named 'first_table' in the specified database in your MySQL server.
-- The database name should be passed as an argument to the mysql command.
-- Description of 'first_table':
--   - id INT
--   - name VARCHAR(256)
-- If the table 'first_table' already exists, the script will not fail.
-- You are not allowed to use the SELECT or SHOW statements.

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);

