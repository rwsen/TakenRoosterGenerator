import MySQLdb as sql

con = sql.connect(username="root", passwd="wortel")
cur = con.cursor()
cur.execute('CREATE DATABASE taken;')

print("much succes")
