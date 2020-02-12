import grpc
from concurrent import futures
import time

# import the generated classes
from example import calculator_pb2, calculator
from example import calculator_pb2_grpc


# 创建一个类来定义服务器功能
# 派生自Calculator_pb2_grpc.CalculatorServicer
class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):

    # 公开 Calculator.square_root
    # 请求和响应属于数据类型,生成Calculator_pb2.Number
    def SquareRoot(self, request, context):
        response = calculator_pb2.Number()
        response.value = calculator.square_root(request.value)
        return response


# 创建一个gRPC服务器
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# 使用生成的函数`add_CalculatorServicer_to_server`
# 将定义的类添加到创建的服务器
calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# server.start不会阻塞,添加了一个睡眠循环以保持
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
