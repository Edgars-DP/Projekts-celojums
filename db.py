import sqlite3
# Datubāzes savienojums un manaģēšana.
# Importē šo failu lai izmantotu

# 1. izveido savienojumu ar lokālu failu
con = sqlite3.connect('data.db')
tr = con.cursor()

# 2. Izveido noklusējuma datus

# Valstis piedzīvijumu ekarānā
tr.execute("""
CREATE TABLE IF NOT EXISTS valstis (vards text, apraksts text, bilde text);
""")

if(len(tr.execute("SELECT * FROM valstis").fetchall()) == 0):
	# Noklusējuma vērtības ja pirmo reizi izveido
	tr.execute("""
		INSERT INTO valstis (vards, apraksts, bilde) 
			VALUES 
				("valsts1", "apraksts1 Lorem ipsum", "bilde1"),
				("valsts2", "apraksts2 Lorem ipsum", "bilde2"),
				("valsts3", "apraksts3 Lorem ipsum", "bilde3"),
				("valsts4", "apraksts4 Lorem ipsum", "bilde4"),
				("valsts5", "apraksts5 Lorem ipsum", "bilde5")
	""")

# Administratora pieejas
tr.execute("""
DROP TABLE IF EXISTS admins;
""")
tr.execute("""
CREATE TABLE admins (sesija text);
""")

con.commit()

con.close()