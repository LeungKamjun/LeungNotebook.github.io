import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 9000))
with open('clientsend/20230525162142.png', 'rb') as stream:
    while True:
        file_data = stream.read(1024)
        if not file_data:
            sk.send(b'q')
            break
        sk.send(file_data)

res = sk.recv(1024)
print('发送成功' if res == b'1' else '发送失败')
sk.close()
