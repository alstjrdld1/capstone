import socket
import select

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('192.168.50.1', 8080))

address = ('192.168.50.1', 8080)

while True:
    data, addr = sock.recvfrom(1024)
    if data:
        print("filename", data)
        file_name = data.strip()
    
    f = open('frames/{}'.format(file_name), 'wb')
    
    while True:
        ready = select.select([sock], [], [], 3)
        if ready[0]:
            data, addr = sock.recvfrom(1024)
            f.write(data)
        else:
            print("Finish", file_name)
            f.close()
            break
    sock.close()

