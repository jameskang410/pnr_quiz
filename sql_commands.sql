DELETE FROM pnr.pnr_quotes WHERE quotes_key = 29;
DELETE FROM pnr.pnr_quotes WHERE quotes_key = 30;
DELETE FROM pnr.pnr_quotes WHERE quotes_key = 31;
DELETE FROM pnr.pnr_quotes WHERE quotes_key = 32;
DELETE FROM pnr.pnr_quotes WHERE quotes_key = 33;
DELETE FROM pnr.pnr_quotes WHERE quotes_key = 34;

--Start PKs over
ALTER TABLE pnr.pnr_quotes DROP COLUMN quotes_key;
ALTER TABLE pnr.pnr_quotes ADD COLUMN quotes_key serial NOT NULL PRIMARY KEY;

SELECT * FROM pnr.pnr_quotes