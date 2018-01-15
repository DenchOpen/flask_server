DROP DATABASE IF EXISTS zhifoudb;

CREATE DATABASE IF NOT EXISTS zhifoudb
  DEFAULT CHARSET utf8
  COLLATE utf8_general_ci;

GRANT ALL PRIVILEGES ON *.* TO 'dench'@'localhost' IDENTIFIED BY '123456';

CREATE TABLE users (
  `id`         VARCHAR(50)  NOT NULL,
  `email`      VARCHAR(50)  NOT NULL,
  `passwd`     VARCHAR(50)  NOT NULL,
  `admin`      BOOL         NOT NULL,
  `name`       VARCHAR(50)  NOT NULL,
  `image`      VARCHAR(500) NOT NULL,
  `created_at` REAL         NOT NULL,
  UNIQUE KEY `idx_email` (`email`),
  KEY `idx_created_at` (`created_at`),
  PRIMARY KEY (`id`)
)
  ENGINE = innodb
  DEFAULT CHARSET = utf8;
