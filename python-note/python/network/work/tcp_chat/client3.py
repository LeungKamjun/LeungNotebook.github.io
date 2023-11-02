import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 9000))
client_id = b'3'

while True:
    inp = input('>>>').encode('utf-8')
    sk.send(b'%s%s' % (client_id, inp))
    if inp.upper() == b'Q':
        break
    msg = sk.recv(1024).decode('utf-8')
    print(msg)
    if msg.upper() == b'Q':
        break

sk.close()
