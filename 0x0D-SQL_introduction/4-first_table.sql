-- creates a table in a database
-- should not throw an error if the table exists
CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	NAME VARCHAR(256)
);
