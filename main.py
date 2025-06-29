import grpc
from concurrent import futures
import tool_pb2
import tool_pb2_grpc

class AIToolServicer(tool_pb2_grpc.AIToolServicer):
    def ProcessMessage(self, request, context):
        return tool_pb2.ToolResponse(response=f"Tool2 processed: {request.message[::-1]}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tool_pb2_grpc.add_AIToolServicer_to_server(AIToolServicer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print('AI Tool 2 running on port 50052')
    server.wait_for_termination()

if __name__ == '__main__':
    serve()