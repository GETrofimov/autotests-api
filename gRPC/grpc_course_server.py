from concurrent import futures

import grpc

import course_service_pb2
import course_service_pb2_grpc

class CourseServiceServicer (course_service_pb2_grpc.CourseServiceServicer):
    def GetCourse(self, request, context):
        
        return course_service_pb2.GetCourseResponse(
             course_id=request.course_id,
             title="Автотесты API",
             description="Будем изучать написание API автотестов"
        )
        
def serve():
        # Создали cервер
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

        # Зареггистрировали сервис
        course_service_pb2_grpc.add_CourseServiceServicer_to_server(CourseServiceServicer(), server)

        # Создали незащищенное соединение
        server.add_insecure_port('[::]:50051')

        #Запускаем сервер
        server.start()
        print("gRPC сервер запущен на порту 50051...")

        #Останавливаем сервер 
        server.wait_for_termination()

# Запуск сервера при выполнении скрипта
if __name__ == "__main__":
    serve()