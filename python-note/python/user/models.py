class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        if username == self.username and password == self.password:
            print('登陆成功')
        else:
            print('登录失败')

    def show(self):
        print(self.username, '' + self.password)
