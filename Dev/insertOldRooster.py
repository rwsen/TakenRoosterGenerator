#insert rooster weeks 28-35
import MySQLdb

#open connection to mysql server
conn = MySQLdb.connect (host = "localhost",
						user = "root",
						passwd = "wortel",
						db = "test")
cursor = conn.cursor ()

cursor.execute("""
	INSERT INTO rooster (weeknummer, jaarnummer, taakID, personID, uitgevoerd)
	VALUES
		(33, 2015, 16, 9, 0)
""")