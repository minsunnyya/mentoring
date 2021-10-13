USE mentoring01

CREATE TABLE User(
id varchar(255),
name varchar(255),
age int
);

show tables;

INSERT INTO User(name, id,age) VALUES('sunday','myId',20);
INSERT INTO User(name, id,age) VALUES('line','herId',40);
INSERT INTO User(name, id,age) VALUES('naver','7Id',7);
INSERT INTO User(name, id,age) VALUES('google','frgre',8);
INSERT INTO User(name, id,age) VALUES('kakao','wev',55);
INSERT INTO User(name, id,age) VALUES('samsung','we',87);
INSERT INTO User(name, id,age) VALUES('LG','ggg',14);

SELECT * FROM User;

