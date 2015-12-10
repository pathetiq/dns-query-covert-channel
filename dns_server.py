'''
Created on 2015-11-27

@author: Based on http://www.wellho.net/resources/ex.php4?item=y303/udp_server.py
'''

import socket

socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# DNS listener on 53
listen_on = ("",53)
socket.bind(listen_on)

while True:
	data,source = socket.recvfrom(1024)
        print data.strip()
