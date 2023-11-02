import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 9002))
sk.listen()
while True:
    conn, addr = sk.accept()
    print(conn)
    while True:
        msg = conn.recv(1024).decode('utf-8')
        print(msg)
        if msg.upper() == 'Q':
            break
        inp = input('>>>')
        conn.send(inp.encode('utf-8'))
        if inp.upper() == 'Q':
            break
    conn.close()
sk.close()
