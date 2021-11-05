import sqlite3
# Datubāzes savienojums un manaģēšana.
# Importē šo failu lai izmantotu

# 1. izveido savienojumu ar lokālu failu
con = sqlite3.connect('data.db')
tr = con.cursor()

# 2. Izveido noklusējuma datus

tr.execute("DROP TABLE valstis;")

tr.execute("""
CREATE TABLE IF NOT EXISTS valstis (vards text, apraksts text, bilde text);
""")

tr.execute("""
INSERT OR IGNORE INTO valstis (vards, apraksts, bilde) 
	VALUES 
		("valsts1", "apraksts1 Lorem ipsum", "bilde1"),
		("valsts2", "apraksts2 Lorem ipsum", "bilde2"),
		("valsts3", "apraksts3 Lorem ipsum", "bilde3"),
		("valsts4", "apraksts4 Lorem ipsum", "bilde4"),
		("valsts5", "apraksts5 Lorem ipsum", "bilde5")
""")

con.commit()

def db_exec(query):
	return tr.execute(query)