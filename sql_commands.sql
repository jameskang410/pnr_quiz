DELETE FROM pnr.pnr_quotes WHERE quotes_key = 35;

--Start PKs over
ALTER TABLE pnr.pnr_quotes DROP COLUMN quotes_key;
ALTER TABLE pnr.pnr_quotes ADD COLUMN quotes_key serial NOT NULL PRIMARY KEY;