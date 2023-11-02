import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()
conn, addr = sk.accept()

with open('serverrecv/20230525162142.png', 'wb') as stream:
    while True:
        file_data = conn.recv(1024)
        if file_data == b'q':
            print('接收成功')
            break
        result = stream.write(file_data)
        print(result)

msg = b'1'
conn.send(msg)
conn.close()
sk.close()
