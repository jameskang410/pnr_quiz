import keyring
import psycopg2

def insert_quote(character, quote):

    password = keyring.get_password('do','database')
    host = keyring.get_password('do','host')

    conn = psycopg2.connect(dbname='django',
                            user='django',
                            host=host,
                            password=password)

    cursor = conn.cursor()

    statement = "INSERT INTO pnr_quotes VALUES ($$%s$$,$$%s$$)" % (character, quote)
    try:
        cursor.execute(statement)
        conn.commit()
        print('Character: %s\nQuote: "%s"' % (character, quote))
    except:
        print('Quote upload failed')

# insert_quote('Leslie Knope','Boring is my middle name')
# insert_quote('Harris Wittels',"I have one testicle--Whac-A-Mole accident--and I'm down to clown")