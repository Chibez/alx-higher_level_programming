-- Computes the score average of all records in the table 'second_table' of the database 'hbtn_0c_0' in your MySQL server.
-- The result column name is 'average'.
-- The database name should be passed as an argument to the mysql command.

SELECT AVG(score) AS average FROM second_table;
