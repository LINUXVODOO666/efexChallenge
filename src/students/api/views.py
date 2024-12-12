from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from students.application.actions import GetAllStudents, CreateStudent, GetStudentById, UpdateStudentById
from students.infrastructure.serializers import StudentSerializer
from students.domain.schemas import SchemaStudent, SchemaStudentUpdate
from config import configure_inject

configure_inject()

# View for managing student-related requests
class Student(APIView):
    
    # Retrieves all students
    def get(self, request):
        students = GetAllStudents().execute()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    # Creates a new student
    def post(self, request):
        try:
            student_data = SchemaStudent(many=False).load(request.data)
            student = CreateStudent().execute(student_data)
            serializer = StudentSerializer(student)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
# View for handling requests for a student by ID
class StudentById(APIView):
    
    # Retrieves a student by ID
    def get(self, request, student_id: int):
        try:
            student = GetStudentById().execute(student_id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    # Updates a student's data by ID
    def patch(self, request, student_id: int):
        try:
            student_data = SchemaStudentUpdate(many=False).load(request.data)
            student = UpdateStudentById().execute(student_id, student_data)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
