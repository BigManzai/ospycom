#!/usr/bin/python

# OpenSim Python send command to screen
# function:
# ./ospycom.py "test" "test123" "alert" "Hello World"
# files:
# ospycom.py ospycom.ini ospycommands.txt

import os
import configparser
import sys

# Passwortabfrage
#def ospycom():
config = configparser.ConfigParser()
config.sections()
config.read('ospycom.ini')
User = config['DEFAULT']['User']
Password = config['DEFAULT']['Password']
Screenname = config['DEFAULT']['Screenname']

os_userlist1 = sys.argv[1]
os_user = ''.join(os_userlist1)
os_userlist2 = sys.argv[2]
os_password = ''.join(os_userlist2)
os_userlist3 = sys.argv[3]
os_os_user = ''.join(os_userlist3)
os_userlist4 = sys.argv[4]
os_parameter = ''.join(os_userlist4)
# print os_user
# print os_password
# print os_os_user
# print os_parameter

if os_user <> User:
	#print "Benutzer stimmt nicht"
	sys.exit(1)
	
if os_password <> Password:
	#print "Password stimmt nicht" 
	sys.exit(1)

os_userexecute = os_os_user + " " + os_parameter

# test ist die testausgabe
#test = 'screen -S '+ Screenname +' -p 0 -X eval "stuff ' "'" + os_userexecute + "'" '^M"'
#print test

# Befehlskette senden:
os.system('screen -S '+ Screenname +' -p 0 -X eval "stuff ' "'" + os_userexecute + "'" '^M"')
