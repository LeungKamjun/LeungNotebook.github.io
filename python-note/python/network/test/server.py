import socket
import struct
import json
import time

sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()
conn, addr = sk.accept()
size = struct.unpack('i', conn.recv(4))[0]
msg = json.loads(conn.recv(size).decode('utf-8'))
print(msg)

