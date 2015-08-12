#! /usr/bin/python

#run.py by Rick Sen
#draai dit script om het takenrooster te genereren

import MySQLdb
import datetime
from random import shuffle

def calculateTaskIDs(weekNumber, cursor):
	list = []
	cursor.execute ("SELECT id, regelmaat FROM taken")
	while (1):
		row = cursor.fetchone ()
		if row == None:
			break
		if weekNumber%row[1]==0:
			list.append(row[0])
	
	return list


def calculateWeek (date, cursor):
	weekNumber = date.isocalendar()[1]
	taskIDList = calculateTaskIDs(weekNumber, cursor)
	#get workers(amount, date, SQLcursor)
	workerIDList = getWorkers(len(taskIDList), date, cursor)
	
	print workerIDList
	
	#randomize the worker list
	shuffle(workerIDList)
	
	#Todo: build the roster
	for taskID in taskIDList:
		sqlString = "INSERT INTO rooster (weeknummer, taakID, personID, uitgevoerd) VALUES (%s, %s, %s, %s)" % (weekNumber, taskID, workerIDList.pop()[1], False)
		cursor.execute(sqlString)
	
	cursor.execute("SELECT * FROM rooster")
	while (1):
		row = cursor.fetchone ()
		if row == None:
			break
		print "%s, %s, %s, %s" % (row[0], row[1], row[2], row[3])
		
		
	return

	
def getWorkers(amount, date, cursor):
	#get all personIDs
	IDList = getAllPersonID(cursor)
	
	#get all onbeschikbaar for current week
	onbeschikbaarList = getAllOnbeschikbaar(date, cursor)
	
	#subtract onbeschikbaarList from IDList
	for personID in onbeschikbaarList:
		if personID in IDList:
			IDList.remove(personID)
	
	
	#get scores to all personIDs
	cursor.execute("""SELECT personID, aantal FROM punten""")
	scoreIDsList = []
	while (1):
		row = cursor.fetchone ()
		if row == None:
			break
		if row[0] in IDList: #test availability
			tempTuple = (int(row[1]), int(row[0]))
			scoreIDsList.append(tempTuple)
			
	# sort the list
	sortedList = sorted(scoreIDsList, key=lambda t:t[0])
	
	
	return sortedList[:amount]

def getAllPersonID (cursor):
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
	
	return IDList
	
def getAllOnbeschikbaar (date, cursor):
	currentWeek = date.isocalendar()[1]
	currentYear = date.isocalendar()[0]
	sqlString = "SELECT personID FROM onbeschikbaar WHERE week=%s AND jaar=%s" % (currentWeek, currentYear)
	cursor.execute(sqlString)
	onbeschikbaarList = []
	while (1):
		row = cursor.fetchone ()
		if row == None:
			break
		(number,) = row
		onbeschikbaarList.append(int(number))
	
	
	return onbeschikbaarList
	
#open connection to mysql server
conn = MySQLdb.connect (host = "localhost",
						user = "root",
						passwd = "wortel",
						db = "test")
cursor = conn.cursor ()


#get weeknumber and year
dateToday = datetime.date.today()
currentWeek = dateToday.isocalendar()[1]

#add 21 days to the dateToday, to get a future weeknumber
dateFuture = dateToday + datetime.timedelta(21)

#test is there is a rooster for the current week
cursor.execute("""
					SELECT weeknummer FROM rooster
""")

#check for current weeknumber in rooster
absent = True
while (1):
	row = cursor.fetchone ()
	if row == None:
		break
	if row == currentWeek:
		absent = False
	print "%s" % (row[0])

#calculate rooster
if absent:
	calculateWeek(dateToday, cursor)

#close connection to mysql server
conn.commit ()
cursor.close ()
conn.close ()


print("much succes")