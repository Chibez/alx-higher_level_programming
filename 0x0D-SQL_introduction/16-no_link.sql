-- Lists all records of the table 'second_table' of the database 'hbtn_0c_0' in your MySQL server.
-- Rows without a name value are not listed.
-- Results display the score and the name, in that order.
-- Records are listed by descending score.
-- The database name should be passed as an argument to the mysql command.

SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
