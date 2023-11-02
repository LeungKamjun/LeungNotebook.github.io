import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()
sk.setblocking(False)

conn_list = []
conn_del = []
while True:
    try:
        # 错误抑制，检查是否有客户端链接
        conn, addr = sk.accept()
        print(conn)
        conn_list.append(conn)
    except BlockingIOError:
        for c in conn_list:
            try:
                # 检查客户端是否有发送消息
                print(1)
                msg = c.recv(1024).decode('utf-8')
                if not msg:
                    # 检查客户端是否断开链接
                    conn_del.append(c)
                    continue
                print('---->',[msg])
                c.send(msg.upper().encode('utf-8'))
            except BlockingIOError:
                print(2)
                pass
        for c in conn_del:
            conn_list.remove(c)
        conn_del.clear()
