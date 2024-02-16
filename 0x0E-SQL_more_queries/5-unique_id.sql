-- Creates the table unique_id on your MySQL server.
-- unique_id description: id INT with the default value 1 and must be unique, name VARCHAR(256).
-- The database name should be passed as an argument to the mysql command.
-- If the table unique_id already exists, the script should not fail.

CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
