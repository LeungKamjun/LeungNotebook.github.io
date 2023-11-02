import socket
import time

sk = socket.socket()
sk.connect(('127.0.0.1', 9000))
for i in range(30):
    time.sleep(0.2)
    # sk.send(b'client111')
    msg = sk.recv(1024)
    print(msg)

