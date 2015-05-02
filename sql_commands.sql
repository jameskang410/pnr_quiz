--Start PKs over
ALTER TABLE pnr.pnr_quotes DROP COLUMN quotes_key;
ALTER TABLE pnr.pnr_quotes ADD COLUMN quotes_key serial NOT NULL PRIMARY KEY;


SELECT * FROM pnr.pnr_quotes;




--for user submissions
SELECT * FROM pnr.pnr_quotes_user;

DELETE FROM pnr.pnr_quotes_user WHERE quotes_key = 1;
DELETE FROM pnr.pnr_quotes_user WHERE quotes_key = 2;

ALTER TABLE pnr.pnr_quotes_user DROP COLUMN quotes_key;
ALTER TABLE pnr.pnr_quotes_user ADD COLUMN quotes_key serial NOT NULL PRIMARY KEY;



DELETE FROM pnr.pnr_quotes_user;






--ADDS USERS' QUOTES INTO ACTUAL QUIZ
INSERT INTO pnr.pnr_quotes SELECT * FROM pnr.pnr_quotes_user;