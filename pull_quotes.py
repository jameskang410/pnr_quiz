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
insert_quote('Ben Wyatt',"Oh, okay, I don't even have time to tell you how wrong you are... actually, it's gonna bug me if I don't. The Lannisters, while very wealthy, do not possess the magical abilities of, say, the warlocks of Qarth, for example")
insert_quote('Tom Haverford', "One time my refrigerator stopped working and I had no idea what to do! I just moved!")
insert_quote('Andy Dwyer','All my favorite foods have butter on them; pancakes, toast, popcorn, grapes -- Oh! Butter is my favorite food!')
insert_quote('Garth Blundin','If he holds the reality gem, that means he can jump from different realities')
insert_quote('April Ludgate',"It's my favorite kind of battle. Two men enter. One me leaves!")
insert_quote('Tom Haverford','I made two pile files')
insert_quote('Andy Dwyer',"One, three, seven, two, five, nine. Pffft! Sudoku is easy. Are there even rules to this game?")
insert_quote('Jerry Gergich',"The hug machine is here! Smiling on all cylinders!")
insert_quote('Andy Dwyer',"Rat Mouse? Rat bastards!")
insert_quote('Chris Traeger','Way to be, duck!')
insert_quote('Mona-Lisa Saperstein',' How did I not know that Diddy was on Instagram, you jagweeds?!')
insert_quote('Mona-Lisa Saperstein','What the mother effing, c-ing ess-ing, effing k-ing EFF is going on right now?!')