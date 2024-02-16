-- Updates the score of Bob to 10 in the table 'second_table'.
-- You are not allowed to use Bob’s id value, only the name field.
-- The database name should be passed as an argument to the mysql command.

UPDATE second_table SET score=10 WHERE name="Bob";
