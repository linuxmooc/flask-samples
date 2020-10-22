DROP DATABASE IF EXISTS school;
CREATE DATABASE school;
USE school;

CREATE TABLE students(
    sno INT,
    name VARCHAR(255),
    age INT,
    PRIMARY KEY(sno)
);

INSERT students(sno, name, age) VALUES(1, 'tom', 11);
INSERT students(sno, name, age) VALUES(2, 'jerry', 12);
INSERT students(sno, name, age) VALUES(3, 'mike', 13);
