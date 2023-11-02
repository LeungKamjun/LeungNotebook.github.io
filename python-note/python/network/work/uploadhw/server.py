import json
import os
import socket
import struct
from pathlib import Path


# 用户验证方法
def login_check(username, password):
    with open('./login_check.txt', 'rb') as steam:
        for i in steam.readlines():
            # 转换成utf-8编码并去掉空格
            i = i.decode('utf-8').strip()
            # 分割账号密码
            lc_username, lc_password = i.split(':')
            if lc_username == username and lc_password == password:
                return True
        else:
            return False


# 绑定服务
sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()
conn, _ = sk.accept()
# 检查登录
while True:
    # 发送登录提示
    login_msg = json.dumps('请登录')
    byte_len = struct.pack('i', len(login_msg))
    conn.send(byte_len)
    conn.send(login_msg.encode('utf-8'))
    # 接受客户端登录请求
    byte_len = conn.recv(4)
    size = struct.unpack('i', byte_len)[0]
    date = json.loads(conn.recv(size))
    # 进行登录挑战
    if login_check(date['username'], date['password']):
        # 发送登录成功信息 , 并通过登录
        msg = json.dumps([1, '登录成功'])
        byte_len = struct.pack('i', len(msg))
        conn.send(byte_len)
        conn.send(msg.encode('utf-8'))
        print(f"{date['username']}登录成功")
        break
    else:
        # 发送登录失败信息，并继续进行挑战
        msg = json.dumps([0, '登录失败'])
        byte_len = struct.pack('i', len(msg))
        conn.send(byte_len)
        conn.send(msg.encode('utf-8'))
        print(f"{date['username']}登录失败")

# 文件上传和下载
while login_check(date['username'], date['password']):
    # 接受文件操作类型
    size = struct.unpack('i', conn.recv(4))[0]
    choice = int(json.loads(conn.recv(size)))
    if choice == 1:
        # 接收文件信息
        byte_len = struct.unpack('i', conn.recv(4))[0]
        file_inf = json.loads(conn.recv(byte_len))
        print(file_inf)
        with open(rf"serverfile/{file_inf['filename']}", 'wb') as stream:
            for i in range((file_inf['size'] // 1024) + 1):
                file_data = conn.recv(1024)
                result = stream.write(file_data)
        if Path(rf"serverfile/{file_inf['filename']}").stat().st_size == file_inf['size']:
            # 发送上传成功信息
            msg = json.dumps('上传成功')
            byte_len = struct.pack('i', len(msg))
            conn.send(byte_len)
            conn.send(msg.encode('utf-8'))
            print(f"{date['username']}上传成功")
        else:
            # 发送上传失败信息
            msg = json.dumps('上传失败')
            byte_len = struct.pack('i', len(msg))
            conn.send(byte_len)
            conn.send(msg.encode('utf-8'))
    elif choice == 2:
        # 列出文件列表
        files_list = os.listdir('serverfile')
        json_data_fl = json.dumps(files_list).encode('utf-8')
        byte_len = struct.pack('i', len(json_data_fl))
        conn.send(byte_len)
        conn.send(json_data_fl)
        # 接收需要传输文件
        byte_len = conn.recv(4)
        size = struct.unpack('i', byte_len)[0]
        download_file = json.loads(conn.recv(size))
        print(download_file)
        file_path = Path(rf'serverfile/{download_file}')
        # 开始传输文件
        # 编写并发送文件信息的json数据
        file_inf = json.dumps({'size': file_path.stat().st_size})
        byte_len = struct.pack('i', len(file_inf))
        conn.send(byte_len)
        conn.send(file_inf.encode('utf-8'))
        # 发送文件
        with open(file_path, 'rb') as stream:
            for i in range((file_path.stat().st_size // 1024) + 1):
                file_data = stream.read(1024)
                conn.send(file_data)
        # 接收登录结果信息
        byte_len = conn.recv(4)
        size = struct.unpack('i', byte_len)[0]
        data = json.loads(conn.recv(size))
        print(data)
    elif choice == 3:
        break

conn.close()
sk.close()
