import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 9000))
while True:
    data, client_addr = sk.recvfrom(1024)
    print(client_addr)
    client_id = int(data.decode('utf-8')[0])
    msg = data.decode('utf-8')[1:]
    print(f'\033[0;3{client_id - 1}mclient{client_id}：{msg}\033[0m')
    if msg.upper() == 'Q':
        rche = '断开'.encode('utf-8')
    else:
        rche = '收到'.encode('utf-8')
    sk.sendto(rche, client_addr)
