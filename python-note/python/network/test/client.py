import socket
import json
import struct
import time

sk = socket.socket()
sk.connect(('127.0.0.1', 9000))
msg = [1, 2, 3, 4, 5, 6]
json_msg = json.dumps(msg).encode('utf-8')
byte_len = struct.pack('i', len(json_msg))
print(type(json_msg))
print(json_msg)
sk.send(byte_len)
sk.send(json_msg)
