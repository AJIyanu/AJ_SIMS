-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS sims CHARACTER SET utf8;
CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'pwd';
GRANT ALL PRIVILEGES ON `sims`.* TO 'admin'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'admin'@'localhost';
FLUSH PRIVILEGES;
