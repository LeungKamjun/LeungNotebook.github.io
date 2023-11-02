import socket
import json


def login_check(username, password):
    with open('login_check.txt', 'rb') as stream:
        a = stream.readlines()
        for i in a:
            i = i.decode('utf-8')
            ru = i.find(':')
            rp = i.find('\r')
            lc_username = i[0:ru]
            lc_password = i[ru + 1:rp]
            # print(lc_username, lc_password)
            if username == lc_username and password == lc_password:
                return b'1'
        else:
            return b'2'


# print(login_check('root', 'b4b8daf4b8ea9d39568719e1e320076f'))
sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()
conn, addr = sk.accept()
data = json.loads(conn.recv(1024))
username = data['username']
password = data['password']
res = login_check(username, password)
print('登录成功' if res == b'1' else '登录失败')
conn.send(res)
conn.close()
sk.close()
