'''
Created on 2015-11-27

@author: Based on http://www.wellho.net/resources/ex.php4?item=y303/udp_server.py
'''

import socket
import argparse

parser = argparse.ArgumentParser(description='Process args.')
parser.add_argument('-p','--port', help='DNS server port', required=True)
args = parser.parse_args()
dns_port = args.port.encode('utf-8')

socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# DNS listener on 53
listen_on = ("",int(dns_port))
socket.bind(listen_on)

while True:
    data,source = socket.recvfrom(1024)
    print data.strip()
