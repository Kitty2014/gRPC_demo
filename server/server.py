#! /usr/bin/env python
# -*- coding: utf-8 -*-
import grpc
import time
from concurrent import futures  # 具有线程池和进程池、管理并行编程任务、处理非确定性的执行流程、进程/线程同步等功能
from example import data_pb2
from example import data_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_HOST = 'localhost'
_PORT = '8081'


class FormatData(data_pb2_grpc.FormatDataServicer):
    def DoFormat(self, request, context):
        str = request.text
        return data_pb2.Data(text=str.upper())


def serve():
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=4))  # 最多有多少work并行执行任务
    data_pb2_grpc.add_FormatDataServicer_to_server(FormatData(), grpcServer)  # 添加函数方法和服务器，服务器端会进行反序列化。
    grpcServer.add_insecure_port(_HOST + ':' + _PORT)  # 建立服务器和端口
    grpcServer.start()  # 启动服务端
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpcServer.stop(0)


if __name__ == '__main__':
    serve()
