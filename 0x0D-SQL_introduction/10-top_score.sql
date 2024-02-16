-- Lists all records of the table 'second_table' of the database 'hbtn_0c_0' in your MySQL server.
-- Results display both the score and the name, in that order.
-- Records are ordered by score in descending order (top first).
-- The database name should be passed as an argument to the mysql command.

SELECT score, name FROM second_table ORDER BY score DESC;
