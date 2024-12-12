from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from students.application.actions import GetAllStudents, CreateStudent, GetStudentById, UpdateStudentById
from students.infrastructure.serializers import StudentSerializer
from students.domain.schemas import SchemaStudent, SchemaStudentUpdate
from config import configure_inject

configure_inject()

class Student(APIView):
    def get(self, request):
        students = GetAllStudents().execute()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        try:
            student_data = SchemaStudent(many=False).load(request.data)
            student = CreateStudent().execute(student_data)
            serializer = StudentSerializer(student)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
class StudentById(APIView):
    def get(self,request,student_id: int):
        try:
            student = GetStudentById().execute(student_id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,student_id: int):
        try:
            student_data = SchemaStudentUpdate(many=False).load(request.data)
            student = UpdateStudentById().execute(student_id,student_data)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
