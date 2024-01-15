-- The script below prepares a MySQL server for the project
-- A new user in hbnb_test (in localhost)
-- The password of hbnb test set to hbnb_test_pwd
-- hbnb_test having all privileges on the hbnb_test_db database
-- hbnb_test having SELECT privileges on perfomance_schema db
-- script should not fail

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
