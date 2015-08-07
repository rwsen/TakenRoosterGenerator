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
			(7, 'Keuken: vloer', 1)
			(8, 'Keuken: vloer', 1)
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
			(20, 'Jurriën'),
			(21, 'Thomas'),
			(22, 'Rick'),
			(23, 'Alper'),
			(24, 'Folkert')
	""")
print "%d rows were inserted" % cursor.rowcount

#add table rooster
cursor.execute("""
		CREATE TABLE rooster
		(
			weeknummer INT,
			taakID INT,
			personID INT,
			uitgevoerd BOOL
		)
	""")

#add table score
cursor.execute("""
		CREATE TABLE score
		(
			personID INT,
			score INT
		)
	""")
cursor.execute("""
		INSERT INTO score (personID, score)
		VALUES
			(1, 0),
			(2, 0),
			(3, 0),
			(4, 0),
			(5, 0),
			(6, 0),
			(7, 0),
			(8, 0),
			(9, 0),
			(10, 0),
			(11, 0),
			(12, 0),
			(13, 0),
			(14, 0),
			(15, 0),
			(16, 0),
			(17, 0),
			(18, 0),
			(19, 0),
			(20, 0),
			(21, 0),
			(22, 0),
			(23, 0),
			(24, 0)
	""")


#close connection to mysql server
cursor.close ()
conn.close ()

print("much succes")
