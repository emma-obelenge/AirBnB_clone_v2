#script that prepares a MySQL server for the project:

#A database hbnb_dev_db
#A new user hbnb_dev (in localhost)
#The password of hbnb_dev should be set to hbnb_dev_pwd
#hbnb_dev should have all privileges on the database hbnb_dev_db (and only this database)
#hbnb_dev should have SELECT privilege on the database performance_schema (and only this database)
#If the database hbnb_dev_db or the user hbnb_dev already exists, your script should not fail


#!/usr/bin/env bash
echo "password is: 'hbnb_dev_pwd'"
cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p
echo "now checking if the db exist in mysqldb. Password='hbnb_dev_pwd'"
echo "SHOW DATABASES;" | mysql -uhbnb_dev -p | grep hbnb_dev_db
echo "check completed!"
echo "Now granting neccessary permissions for 'hbnb_dev' user... Password is: 'hbnb_dev_pwd'"
echo "SHOW GRANTS FOR 'hbnb_dev'@'localhost';" | mysql -uroot -p
echo "Permissions granted successfully..."

