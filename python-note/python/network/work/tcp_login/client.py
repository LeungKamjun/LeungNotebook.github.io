import hashlib
import socket
import json


def get_md5(username, password):
    md5 = hashlib.md5(username.encode('utf-8'))
    md5.update(password)
    return md5.hexdigest()


sk = socket.socket()
sk.connect(('127.0.0.1', 9000))
username = input('请输入账号：')
password = input('请输入密码：').encode('utf-8')
json_data = json.dumps({'username': username, 'password': get_md5(username, password)})
print(type(json_data))
sk.send(json_data.encode('utf-8'))
res = sk.recv(1024)
print('登录成功' if res == b'1' else '登录失败')
sk.close()
