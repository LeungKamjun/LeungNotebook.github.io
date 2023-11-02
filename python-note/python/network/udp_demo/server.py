import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 9000))
while True:
    msg, client_addr = sk.recvfrom(1024)
    print(msg.decode('utf-8'))
    msg = input('>>>').encode('utf-8')
    sk.sendto(msg, client_addr)

sk.close()
