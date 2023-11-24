-- Prepare a MySQL server for the project
CREATE DATABASE benfa_db;
CREATE USER 'benfa'@'localhost' IDENTIFIED BY 'kiitos';
GRANT ALL PRIVILEGES ON `benfa_db`.*TO 'benfa'@'localhost';
GRANT SELECT ON `performance_schema`.*TO 'benfa'@'localhost';
FLUSH PRIVILEGES;