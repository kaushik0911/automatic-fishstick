DROP USER IF EXISTS 'cdc_user'@'%';
CREATE USER 'cdc_user'@'%' IDENTIFIED BY 'cdc_pass';
GRANT SELECT, RELOAD, SHOW DATABASES, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'cdc_user'@'%';
FLUSH PRIVILEGES;

CREATE TABLE inventory.products (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255),
  description TEXT,
  price DECIMAL(10,2),
  quantity INT
);

INSERT INTO inventory.products (name, description, price, quantity)
VALUES ('Widget', 'A basic widget', 19.99, 100);
