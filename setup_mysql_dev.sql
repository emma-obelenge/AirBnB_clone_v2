-- Script that prepares a MySQL server for the project

-- create the database (hbnb_dev_db) if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- grant all privileges on the database hbnb_dev_db to user hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- grant select privilege on the database performance_schema to user hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- flush privileges to ensure the new privileges are put into effect
FLUSH PRIVILEGES;
