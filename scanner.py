#!/bin/python3


import sys  #Enabling you to enter new  line
import socket
from datetime import datetime

#Defining our target
if len(sys.argv)==2:
	target=socket.gethostbyname(sys.argv[1])
else:
	print("invaid amount of arguments")
	sys.exit()

print("-" *50)
print("scanning target " +target)
print("Time started " +str(datetime.now()))
print("-" *50)
try:
	#you can specify the range of the port you want in the loop
	for port in range(40,90):
	   s=socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
	   socket.setdefaulttimeout(1) #is float
	   re=s.connect_ex((target,port)) #retruns error indicator
	   print("checking port {} ".format(port))
	   if re ==0:
	   	print("port {} is open ".format(port))
	   s.close()
except KeyboardInterrupt:
	print("Exiting the prog")
	sys,exit()

except socket.gaierror:
	print("hostname could be resolved")
	sys.exit()
except socket.error:
	print("could not conncet to server")
	sys.exit()
