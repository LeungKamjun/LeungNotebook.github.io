import socket
import time

sk = socket.socket()
sk.connect(('127.0.0.1', 9000))
for i in range(50):
    time.sleep(1)
    sk.send(b'client222')
    msg = sk.recv(1024)
    print(msg)
