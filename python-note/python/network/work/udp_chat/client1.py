import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
client_id = b'1'

while True:
    inp = input('>>>').encode('utf-8')
    sk.sendto(b'%s%s' % (client_id, inp),('127.0.0.1', 9000))
    ret = sk.recv(1024).decode('utf-8')
    print(ret)
    if inp.upper() == b'Q':
        break

sk.close()
