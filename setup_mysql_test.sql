-- Task 4:
-- Script that prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- in case of ERROR 1290 (HY000): The MySQL server is running with the
-- skip-grant-tables option, uncomment the next instruction:
-- FLUSH PRIVILEGES;

CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';

GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
