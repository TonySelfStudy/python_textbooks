# Programming Python Example 12-1 Page 788

import sys
from socket import *
import time

serverHost = 'localhost'
myPort = 50007
buff_size = 1024  # max message size in bytes

message = [b'Hello network world']

print(sys.argv)

if len(sys.argv) > 1:
    serverHost = sys.argv[1]
    if len(sys.argv) > 2:
        message = [msg.encode() for msg in sys.argv[2:]]

print(f'Connecting to server: {serverHost} on port {myPort}')
print(f'Going to pass message: {message}')

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, myPort))

for line in message:
    print(f'Sending line in 5 seconds: {line=}')
    time.sleep(5)
    sockobj.send(line)
    data = sockobj.recv(buff_size)
    print(f'Client received: {data}')

sockobj.close()
