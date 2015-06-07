import MySQLdb

#open connection to mysql server
conn = MySQLdb.connect (host = "localhost",
						user = "root",
						passwd = "wortel",
						db = "test")
cursor = conn.cursor ()

#add table taken
cursor.execute("DROP TABLE IF EXISTS taken")
cursor.execute("""
		CREATE TABLE taken
		(
			id INT,
			naam CHAR(40),
			regelmaat INT
		)
	""")
cursor.execute("""
		INSERT INTO taken (id, naam, regelmaat)
		VALUES
			(1, 'WC maandag of dinsdag', 1),
			(2, 'WC donderdag of vrijdag', 1),
			(3, 'Keukenvloer', 1)
	""")
print "%d rows were inserted" % cursor.rowcount

cursor.execute ("SELECT id, naam FROM taken")
while (1):
	row = cursor.fetchone ()
	if row == None:
		break
	print "%s, %s" % (row[0], row[1])
print "%d rows were returned" % cursor.rowcount



#add table mensen




#close connection to mysql server
cursor.close ()
conn.close ()

print("much succes")
