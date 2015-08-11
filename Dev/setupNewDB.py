#! /usr/bin/python

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
			(1, 'Vuilniszakken', 1),
			(2, 'WC maandag of dinsdag', 1),
			(3, 'WC donderdag of vrijdag', 1),
			(4, 'Douchekabines', 1),
			(5, 'Doucheruimte', 1),
			(6, 'Keuken: aanrechten', 1),
			(7, 'Keuken: vloer', 1),
			(8, 'Keuken: vloer', 1),
			(9, 'Trappenhuis', 3),
			(10, 'Trappenhuis', 3),
			(11, 'Ramen', 8),
			(12, 'Keuken: kleine dingen', 1),
			(13, 'Keuken: krattenplank', 2),
			(14, 'Adelaarstraat', 3),
			(15, 'Koekoekstraat', 3),
			(16, 'Lijsterstraat', 3)
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
cursor.execute("DROP TABLE IF EXISTS mensen")
cursor.execute("""
		CREATE TABLE mensen
		(
			personID INT,
			naam CHAR(40)
		)
	""")
cursor.execute("""
		INSERT INTO mensen (personID, naam)
		VALUES
			(1, 'Iris'),
			(2, 'Emmalien'),
			(3, 'Manoushka'),
			(4, 'Annabel'),
			(5, 'Freek'),
			(6, 'Wouter'),
			(7, 'Danique'),
			(8, 'Laura'),
			(9, 'Michel'),
			(10, 'Ilse'),
			(11, 'Michiel'),
			(12, 'Elke'),
			(13, 'Myra'),
			(14, 'Valentijn'),
			(15, 'Koen'),
			(16, 'Limaia'),
			(17, 'Thijmen'),
			(18, 'Tim'),
			(19, 'Paul'),
			(20, 'Jurrien'),
			(21, 'Thomas'),
			(22, 'Rick'),
			(23, 'Alper'),
			(24, 'Folkert')
	""")
print "%d rows were inserted" % cursor.rowcount

#add table rooster
cursor.execute("DROP TABLE IF EXISTS rooster")
cursor.execute("""
		CREATE TABLE rooster
		(
			weeknummer INT,
			taakID INT,
			personID INT,
			uitgevoerd BOOL
		)
	""")

#add table punten
cursor.execute("DROP TABLE IF EXISTS punten")
cursor.execute("""
		CREATE TABLE punten
		(
			personID INT,
			aantal INT,
			tekst CHAR(40)
		)
	""")
cursor.execute("""
		INSERT INTO punten (personID, aantal, tekst)
		VALUES
			(1, 0, 'a'),
			(2, 0, 'a'),
			(3, 0, 'a'),
			(4, 0, 'a'),
			(5, 0, 'a')
			
			
	""")
print "%d rows were inserted" % cursor.rowcount
	
	
#close connection to mysql server
cursor.close ()
conn.close ()

print("much succes")
