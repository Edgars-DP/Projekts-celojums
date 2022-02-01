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
CREATE TABLE IF NOT EXISTS viesnicas (nosaukums text, valsts text, nakts INT);
""")

if(len(tr.execute("SELECT * FROM valstis").fetchall()) == 0):
	# Noklusējuma vērtības ja pirmo reizi izveido
	tr.execute("""
		INSERT INTO valstis (vards, apraksts, bilde) 
			VALUES 
				("ASV", "apraksts1 Lorem ipsum", "bilde1"),
				("Francija", "apraksts2 Lorem ipsum", "bilde2"),
				("Meksika", "apraksts3 Lorem ipsum", "bilde3"),
				("Latvija", "apraksts4 Lorem ipsum", "bilde4");
	""")

if(len(tr.execute("SELECT * FROM viesnicas").fetchall()) == 0):
	# Noklusējuma vērtības ja pirmo reizi izveido
	tr.execute("""
		INSERT INTO viesnicas (nosaukums, valsts, nakts) 
			VALUES 
				("ASV-viesnica1", "ASV", '20'),
				("ASV-viesnica2", "ASV", '30'),
				("ASV-viesnica3", "ASV", '25'),
				("ASV-viesnica4", "ASV", '40'),
				("ASV-viesnica5", "ASV", '200'),
				("francija-viesnica1", "Francija", '25'),
				("francija-viesnica2", "Francija", '35'),
				("francija-viesnica3", "Francija", '25'),
				("francija-viesnica4", "Francija", '45'),
				("francija-viesnica5", "Francija", '205'),
				("meksika-viesnica1", "Meksika", '29'),
				("meksika-viesnica2", "Meksika", '39'),
				("meksika-viesnica3", "Meksika", '29'),
				("meksika-viesnica4", "Meksika", '49'),
				("meksika-viesnica5", "Meksika", '209');
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