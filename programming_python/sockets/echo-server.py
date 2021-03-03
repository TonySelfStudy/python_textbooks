# Programming Python Example 12-1 Page 788

import socket
myHost = ''
myPort = 50007
buff_size = 1024  # max message size in bytes

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("This Computer Name is:" + hostname)
print("This Computer IP Address is:" + IPAddr)


print(f'Creating server: {myHost} on port {myPort}')

sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockobj.bind((myHost, myPort))
sockobj.listen(5)

while True:
    connection, address = sockobj.accept()
    print(f'Server connected by, {address}')

    print(f'{connection=}')
    while True:
        print(f'Waiting to receive data')
        data_receive = connection.recv(buff_size)
        print(f'{data_receive=}')
        data_return = b'Echo=> ' + data_receive

        if data_receive:
            print(f'data to return: {data_return}')
            connection.send(data_return)
        else:
            break
    connection.close()
