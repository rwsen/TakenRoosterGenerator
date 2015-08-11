#! /usr/bin/python

#run.py by Rick Sen
#draai dit script om het takenrooster te genereren

import MySQLdb
import datetime

def calculateTaskIDs(weekNumber):
	list = []
	cursor.execute ("SELECT id, regelmaat FROM taken")
	while (1):
		row = cursor.fetchone ()
		if row == None:
			break
		if weekNumber%row[1]==0:
			list.append(row[0])
	
	return list


def calculateWeek (weekNumber, cursor):
	taskIDList = calculateTaskIDs(weekNumber)
	print len(taskIDList)
	
	getWorkers(len(taskIDList), cursor)
	
	return

	
def getWorkers(amount, cursor):
	cursor.execute("""
						SELECT personID FROM mensen
	""")
	
	#put all personIDs in IDList
	IDList = []
	while (1):
		row = cursor.fetchone ()
		if row == None:
			break
		(number,) = row
		IDList.append(int(number))
	
	print(IDList)
	
	#get scores to all personIDs
	cursor.execute ("SELECT * FROM score")
	scoreIDsList = []
	while (1):
		row = cursor.fetchone ()
		if row == None:
			print("No rows were returned.")
			break
		print("One row was returned.")
		if 1: #test availability
			tempTuple = (int(row[0]))
			scoreIDsList.append(tempTuple)
			
	print(scoreIDsList)
			
	sorted(scoreIDsList, key=lambda score: score[0])   # sort by age
	
	print(scoreIDsList)
	
	return

#open connection to mysql server
conn = MySQLdb.connect (host = "localhost",
						user = "root",
						passwd = "wortel",
						db = "test")
cursor = conn.cursor ()


#get weeknumber and year
dateToday = datetime.date.today()
currentWeek = dateToday.isocalendar()[1]
currentYear = dateToday.isocalendar()[0]

#add 21 days to the dateToday, to get a future weeknumber
dateFuture = dateToday + datetime.timedelta(210)
futureWeek = dateFuture.isocalendar()[1]
futureYear = dateFuture.isocalendar()[0]

#test is there is a rooster for the current week
cursor.execute("""
					SELECT weeknummer FROM rooster
""")

#print weeknumbers
absent = False
while (1):
	row = cursor.fetchone ()
	if row == None:
		break
	if row == currentWeek:
		absent = True
	print "%s" % (row[0])
print "%d rows were returned" % cursor.rowcount

if not absent:
	calculateWeek(currentWeek, cursor)

#close connection to mysql server
cursor.close ()
conn.close ()


print("much succes")