SET character_set_database=utf8;
SET character_set_server=utf8;
DROP DATABASE IF EXISTS todoDB;
CREATE DATABASE todoDB;
USE todoDB;

CREATE TABLE users(
    userId INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255),
    password VARCHAR(255),
    PRIMARY KEY(userId)
);

CREATE TABLE todos(
    todoId INT NOT NULL AUTO_INCREMENT,
    userId INT,
    status VARCHAR(255),
    title VARCHAR(255),
    PRIMARY KEY(todoId)
);

INSERT INTO users(name, password) VALUES ("guest", "123");
INSERT INTO todos(userId, status, title) VALUES (1, "todo", "吃饭");
INSERT INTO todos(userId, status, title) VALUES (1, "todo", "睡觉");
INSERT INTO todos(userId, status, title) VALUES (1, "done", "作业");

