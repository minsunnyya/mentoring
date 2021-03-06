#CRUD
#CREATE, READ, UPDATE, DELETE


#CREATE
SELECT * FROM buyTBL;
INSERT INTO buyTBL VALUES('KMS','김민선',19950625,'광주',010,161,NOW());
INSERT INTO buyTBL VALUES('KMS','김무선',19950713,'성남',011,171,2014-05-06);
INSERT INTO buyTBL VALUES('KKW','김곽용',19980723,'구리',017,181,2021-03-05);

#READ
SELECT addr AS '회원주소지' FROM buyTBL;
SELECT * FROM buyTBL WHERE name LIKE '김%';
SELECT * FROM buyTBL ORDER BY height DESC;


#UPDATE
UPDATE buyTBL  SET userID='KMS' WHERE userID='HI';
UPDATE buyTBL  SET height='171' WHERE height='2m';

#DELETE
DELETE FROM buyTBL WHERE mobile1=10;
