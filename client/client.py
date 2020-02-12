#! /usr/bin/env python
# -*- coding: utf-8 -*-
import grpc
from example import data_pb2, data_pb2_grpc

_HOST = 'localhost'
_PORT = '8081'


def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)  # 服务器信息
    client = data_pb2_grpc.FormatDataStub(channel=conn)  # 客户端建立连接
    for i in range(0, 2):
        respnse = client.DoFormat(data_pb2.Data(text='hello,world!'))  # 序列化数据传递过去
        print("received: " + respnse.text)


if __name__ == '__main__':
    run()
