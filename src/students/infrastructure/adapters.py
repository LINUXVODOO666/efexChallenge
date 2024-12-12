from typing import List, Any, Optional
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from students.infrastructure.models import Student
from students.domain.interfaces import IStudents
from students.domain.exceptions import StudentEmailError, StudentNotExistError

# Class for handling student-related data operations
class AdaStudents:
    
    # Retrieves all students
    def get_all_students(self) -> List[Student]:
        return Student.objects.all()

    # Creates a new student, checks for duplicate email
    def create_student(self, data: dict) -> Student:
        if Student.objects.filter(email=data['email']).exists():
            raise StudentEmailError()  # Raises error if email already exists
        return Student.objects.create(**data)
    
    # Retrieves a student by ID, raises error if not found
    def get_student_by_id(self, student_id: int) -> Student:
        try:
            return Student.objects.get(id=student_id)
        except ObjectDoesNotExist:
            raise StudentNotExistError()  # Raises error if student doesn't exist

    # Updates a student's data by ID, raises errors for missing or invalid data
    def update_student_by_id(self, student_id: int, data: dict) -> bool:
        try:
            student = Student.objects.get(id=student_id)
            for key, val in data.items():
                if val is not None:
                    setattr(student, key, val)
            student.save()
            return student
        
        except ObjectDoesNotExist:
            raise StudentNotExistError()  # Raises error if student doesn't exist
        except IntegrityError:
            raise StudentEmailError()  # Raises error if email conflict occurs
