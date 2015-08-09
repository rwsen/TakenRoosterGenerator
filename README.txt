TakenRoosterGenerator
Programma dat het huistakenrooster voor AL16 G3.4 genereert en presenteert.

Hoe te gebruiken?
- verbind via ssh (putty)
- log in met pi en raspberry
- navigeer naar de map /home/huistaken/TakenRoosterGenerator
- 'sudo git pull', evt nog 'sudo git checkout [branch]'
- de database moet handmatig aangemaakt worden, met de volgende waarden:
	- host = "localhost"
	- user = "root"
	- passwd = "wortel"
	- db = "test"
- run éénmaal 'python setupNewDB.py'. Dit creëert de initiële tabellen:
	- taken
	- mensen
	- rooster
	- score (= aantal gedane taken)
	- TODO beschikbaarheid
	- TODO mailadressen
- run 'run.py' om het takenrooster te genereren.