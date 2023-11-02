import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()
while True:
    conn, addr = sk.accept()
    while True:
        data = conn.recv(1024).decode('utf-8')
        client_id = int(data[0])
        msg = data[1:]
        print(f'\033[0;3{client_id - 1}m{msg}\033[0m')
        if msg.upper() == 'Q':
            break
        inp = input('>>>').encode('utf-8')
        conn.send(inp)
        if inp.upper() == 'Q':
            break
    conn.close()
sk.close()
