-- Task 3:
-- Script that prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- in case of ERROR 1290 (HY000): The MySQL server is running with the
-- skip-grant-tables option, descomment the next instruction:
--FLUSH PRIVILEGES;

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
