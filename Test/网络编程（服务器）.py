#!/usr/bin/python
# encoding=utf-8

import socket

s = socket.socket  # 创建 socket 对象
host =s.gethostname()  # 获取本地主机名
port = 12345  # 设置端口
s.bind(host, port)  # 绑定端口

s.listen(5)  # 等待客户端连接
while True:
    c, addr = s.accept()  # 建立客户端连接。
    print '连接地址：', addr
    c.send('你好，这是服务器端发送的数据')
    c.close()
