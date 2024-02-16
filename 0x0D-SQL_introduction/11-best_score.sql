-- Lists all records with a score greater than or equal to 10 in the table 'second_table' of the database 'hbtn_0c_0' in your MySQL server.
-- Results display both the score and the name, in that order.
-- Records are ordered by score in descending order (top first).
-- The database name should be passed as an argument to the mysql command.

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;

