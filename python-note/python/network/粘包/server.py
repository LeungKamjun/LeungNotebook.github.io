import socket
import time
import struct

sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()

conn, _ = sk.accept()
while True:
    time.sleep(0.1)
    byte_len = conn.recv(4)
    size = struct.unpack('i', byte_len)[0]
    msg = conn.recv(size).decode('utf-8')
    if msg.upper() == 'Q':
        print('我要断开了喔')
        conn.send('断开成功'.encode('utf-8'))
        break
    else:
        print(msg)
conn.close()
sk.close()
