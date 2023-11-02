import socket
import json
import struct
import uuid
import hashlib


def send_msg(msg, conn):
    json_msg = json.dumps(msg)
    byte_len = struct.pack('i', len(json_msg))
    conn.send(byte_len)
    conn.send(json_msg.encode('utf-8'))


def recv_msg(conn):
    size = struct.unpack('i', conn.recv(4))[0]
    msg = json.loads(conn.recv(size).decode('utf-8'))
    return msg


def get_sha256(key, str):
    sha256 = hashlib.sha3_256(key.encode('utf-8'))
    sha256.update(str)
    return sha256.hexdigest()


# 链接服务器
sk = socket.socket()
sk.connect(('127.0.0.1', 9000))

# 生成密钥
key = str(uuid.uuid4())[:4]
# 发送密钥到服务器
send_msg(key, sk)
# 接受服务器发送的随机字符串
ran_str = sk.recv(32)
# 使用密钥对随机字符串进行摘要
hash_str = get_sha256(key, ran_str)
print(hash_str)
# 发送摘要后的数据
send_msg(hash_str, sk)
