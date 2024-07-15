-- prepares a MySQL server for the project
-- SET GLOBAL validate_password.policy = LOW
 
CREATE DATABASE IF NOT EXISTS sync_dev_db;
CREATE USER IF NOT EXISTS 'sync_dev'@'localhost' IDENTIFIED BY 'sync_dev_pwd';
GRANT ALL PRIVILEGES ON `sync_dev_db`.* TO 'sync_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'sync_dev'@'localhost';
FLUSH PRIVILEGES;
