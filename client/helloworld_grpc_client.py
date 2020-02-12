import grpc
# import helloworld_pb2
# import helloworld_pb2_grpc
from example import helloworld_pb2_grpc, helloworld_pb2


def run():
    # 连接 rpc 服务器
    channel = grpc.insecure_channel('localhost:50051')
    # 调用 rpc 服务
    stub = helloworld_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(helloworld_pb2.HelloRequest(name='张三'))
    print("Greeter client received: " + response.message)
    response = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name='王五'))
    print("Greeter client received: " + response.message)
    response = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name='老李'))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    run()
