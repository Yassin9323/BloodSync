-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS sync_test_db;
CREATE USER IF NOT EXISTS 'sync_test'@'localhost' IDENTIFIED BY 'sync_test_pwd';
GRANT ALL PRIVILEGES ON `sync_test_db`.* TO 'sync_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'sync_test'@'localhost';
FLUSH PRIVILEGES;
