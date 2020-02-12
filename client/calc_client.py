import grpc
from example import calculator_pb2
from example import calculator_pb2_grpc

# 打开一个gRPC通道
channel = grpc.insecure_channel('localhost:50051')
# 创建一个存根（客户端）
stub = calculator_pb2_grpc.CalculatorStub(channel)

# 创建有效的请求消息
number = calculator_pb2.Number(value=16)

# 调用
response = stub.SquareRoot(number)
print(response.value)
