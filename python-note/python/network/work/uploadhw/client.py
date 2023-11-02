import hashlib
import json
import socket
import struct
from pathlib import Path
import os


def get_md5(username, password):
    md5 = hashlib.md5(username.encode('utf-8'))
    md5.update(password)
    return md5.hexdigest()


# 链接服务器
sk = socket.socket()
sk.connect(('127.0.0.1', 9000))
# 用户登录
while True:
    # 接受登录提示
    byte_len = sk.recv(4)
    size = struct.unpack('i', byte_len)[0]
    print(json.loads(sk.recv(size)))
    # 输入账号密码
    username = input('请输入用户名：')
    password = input('请输入密码：').encode('utf-8')
    json_user_login = json.dumps({'username': username, 'password': get_md5(username, password)})
    # 发送登录挑战
    byte_len = struct.pack('i', len(json_user_login))
    sk.send(byte_len)
    sk.send(json_user_login.encode('utf-8'))
    # 接收登录结果信息
    byte_len = sk.recv(4)
    size = struct.unpack('i', byte_len)[0]
    data = json.loads(sk.recv(size))
    print(data[1])
    if data[0]:
        break

# 文件上传和下载
while data[0]:
    choice = int(input('1.上传 2.下载 3.退出：'))
    choice_data = json.dumps(choice).encode('utf-8')
    byte_len = struct.pack('i', len(choice_data))
    sk.send(byte_len)
    sk.send(choice_data)
    # 文件上传
    if choice == 1:
        upload_path = Path(input('请输入上传文件绝对路径：'))
        # 判断文件是否为绝对路劲，文件是否存在
        if os.path.isabs(upload_path) and os.path.exists(upload_path):
            # 编写并发送文件信息的json数据
            file_inf = json.dumps({'size': upload_path.stat().st_size, 'filename': os.path.basename(upload_path)})
            byte_len = struct.pack('i', len(file_inf))
            sk.send(byte_len)
            sk.send(file_inf.encode('utf-8'))
            # 读取并发送文件
            with open(upload_path, 'rb') as stream:
                for i in range((upload_path.stat().st_size // 1024) + 1):
                    file_data = stream.read(1024)
                    sk.send(file_data)
            # 接收上传结果信息
            byte_len = sk.recv(4)
            size = struct.unpack('i', byte_len)[0]
            data = json.loads(sk.recv(size))
            print(data)
        else:
            print('输入的不是绝对路径或者文件不存在')
    elif choice == 2:
        # 文件下载
        byte_len = sk.recv(4)
        size = struct.unpack('i', byte_len)[0]
        files_list = json.loads(sk.recv(size))
        print(files_list)
        # 发送需要下载的文件
        download_file = json.dumps(input('请输入要下载的文件名：'))
        size = struct.pack('i', len(download_file))
        sk.send(size)
        sk.send(download_file.encode('utf-8'))
        # 接收文件信息
        size = struct.unpack('i', sk.recv(4))[0]
        file_inf = json.loads(sk.recv(size))
        print(file_inf)
        # 接收文件
        with open(rf"clientdown/{json.loads(download_file)}", 'wb') as stream:
            for i in range((file_inf['size'] // 1024) + 1):
                file_data = sk.recv(1024)
                result = stream.write(file_data)
        # 判断并发送下载是否成功
        if Path(rf"clientdown/{json.loads(download_file)}").stat().st_size == file_inf['size']:
            # 发送上传成功信息
            msg = json.dumps('上传成功')
            byte_len = struct.pack('i', len(msg))
            sk.send(byte_len)
            sk.send(msg.encode('utf-8'))
            print(f"{json.loads(download_file)}下载成功")
        else:
            # 发送上传失败信息
            msg = json.dumps('上传失败')
            byte_len = struct.pack('i', len(msg))
            sk.send(byte_len)
            sk.send(msg.encode('utf-8'))
    elif choice == 3:
        break

sk.close()
