import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 9002))
msg = None
while True:
    inp = input('>>>')
    sk.send(inp.encode('utf-8'))
    if inp.upper() == 'Q':
        break
    msg = sk.recv(1024).decode('utf-8')
    print(msg)
    if msg.upper() == b'Q':
        break

sk.close()
