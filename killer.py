#!/usr/bin/python
#-*- coding:utf8 -*-
#Giacomo Mirabassi <giacomo@mirabassi.it>
#GNU/GPL (http://www.gnu.org)
#ver. 1.1
#Impedisce l'accesso non autorizzato ai programmi
#uso: ./killer.py argomenti
#argomenti=nome del programma da terminare o un gruppo tra questi:
#web, utils, games, default(tutti)
#È possibile specificare anche un utente insieme al processo indicandolo così: processo,utente

import subprocess
import time
import sys
import string

#applications by type
games="gcompris","gnomines","same-gnome","ktuberling","gnibbles","gnometris","sol","iagno","glchess"
web="firefox","firefox-bin"
utils="gnome-appearance-properties","gedit"

argv=sys.argv[1:]
if len(argv)>0:
	killzone=[]
	for arg in argv:
		if arg=="default":
			killzone.extend(games).extend(web).extend(utils)
		elif arg=="web":
			killzone.extend(web)
		elif arg=="utils":
			killzone.extend(utils)
		elif arg=="games":
			killzone.extend(games)
		else:
			killzone.append(arg)
else:
	print "nessun programma o gruppo di programmi specificato"
	quit()
		


print "premere CTRL+C per terminare il programma"

#main loop
while 1>0:
	for app in killzone:
		user=''
		v=string.find(app,',')
		if(v>=0):
			user=app[v:]
			user=user[1:]
			app=app[0:v]
		if(user!=''):
			print "termino "+app+" per "+user
			code=subprocess.call(["killall",app,"-9","-u"+user])
		else:
			print "termino "+app
			code=subprocess.call(["killall",app,"-9"])
		if code==0:
			print "\033[31m terminato "+app+"\033[0m"
	print "premere CTRL+C per terminare il programma"
	time.sleep(20)
