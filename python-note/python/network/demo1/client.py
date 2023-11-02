import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 9000))
msg = None
while True:
    if msg == 'q':
        break
    else:
        inp = input('>>>')
        if inp == 'q' or msg == 'q':
            break
        else:
            sk.send(inp.encode('utf-8'))
            msg = sk.recv(1024)
            print(msg.decode('utf-8'))
sk.close()
