import socket
import struct

sk = socket.socket()
sk.connect(('127.0.0.1', 9000))

while True:
    msg = input('请输入信息：').encode('utf-8')
    byte_len = struct.pack('i', len(msg))
    sk.send(byte_len)
    sk.send(msg)
    if msg.decode('utf-8').upper() == 'Q':
        print(sk.recv(1024).decode('utf-8'))
        break
sk.close()
