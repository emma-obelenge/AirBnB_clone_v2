-- Script that prepares a MySQL server for the project

-- create or use database(hbnb_test_db)
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create the user with the specified password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- grant all privileges on the database hbnb_test_db to user hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- grant select privilege on performance_schema to user hbnb_test
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- flush privileges to ensure new privileges are put to effect
FLUSH PRIVILEGES;
