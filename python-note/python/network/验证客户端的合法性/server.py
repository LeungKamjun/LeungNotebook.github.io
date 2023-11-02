import hashlib
import os
import socket
import json
import struct


def send_msg(msg, conn):
    json_msg = json.dumps(msg).encode('utf-8')
    byte_len = struct.pack('i', len(json_msg))
    conn.send(byte_len)
    conn.send(json_msg)


def recv_msg(conn):
    size = struct.unpack('i', conn.recv(4))[0]
    msg = json.loads(conn.recv(size).decode('utf-8'))
    return msg


def get_sha256(key, str):
    sha256 = hashlib.sha3_256(key.encode('utf-8'))
    sha256.update(str)
    return sha256.hexdigest()


# 启动网络服务
sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()
conn, addr = sk.accept()
# 接受客户端发送的密钥
key = recv_msg(conn)
# 生成随机字符串并发送
ran_str = os.urandom(32)
conn.send(ran_str)
# 使用密钥对随机字符串进行摘要
hash_str = get_sha256(key, ran_str)
# 接受客户端发送的摘要数据
client_hash = recv_msg(conn)
if hash_str == client_hash:
    print('合法客户端')
else:
    print('非法客户端')
