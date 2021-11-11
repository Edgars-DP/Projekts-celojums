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

tr.execute("""
CREATE TABLE IF NOT EXISTS viesnicas (nosaukums text, valsts text);
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

if(len(tr.execute("SELECT * FROM viesnicas").fetchall()) == 0):
	# Noklusējuma vērtības ja pirmo reizi izveido
	tr.execute("""
		INSERT INTO viesnicas (nosaukums, valsts) 
			VALUES 
				("ASV-viesnica1", "ASV"),
				("ASV-viesnica2", "ASV"),
				("ASV-viesnica3", "ASV"),
				("ASV-viesnica4", "ASV"),
				("ASV-viesnica5", "ASV"),
				("francija-viesnica1", "Francija"),
				("francija-viesnica2", "Francija"),
				("francija-viesnica3", "Francija"),
				("francija-viesnica4", "Francija"),
				("francija-viesnica5", "Francija"),
				("meksika-viesnica1", "Meksika"),
				("meksika-viesnica2", "Meksika"),
				("meksika-viesnica3", "Meksika"),
				("meksika-viesnica4", "Meksika"),
				("meksika-viesnica5", "Meksika");
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