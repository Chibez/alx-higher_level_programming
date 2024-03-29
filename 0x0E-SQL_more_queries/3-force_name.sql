-- Creates the table force_name on your MySQL server.
-- force_name description: id INT, name VARCHAR(256) Not Null.
-- The database name should be passed as an argument to the mysql command.
-- If the table force_name already exists, the script should not fail.

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);

