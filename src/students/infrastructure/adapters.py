from typing import List, Any, Optional
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist


from students.infrastructure.models import Student
from students.domain.interfaces import IStudents
from students.domain.exceptions import StudentEmailError, StudentNotExistError

class AdaStudents:
    def get_all_students(self) -> List[Student]:
        return Student.objects.all()

    def create_student(self, data:dict) -> Student:
        if Student.objects.filter(email = data['email']).exists():
            raise StudentEmailError()
        return Student.objects.create(**data)
    
    def get_student_by_id(self, student_id:int) -> Student:
        try:
            return Student.objects.get(id = student_id)
        except ObjectDoesNotExist:
            raise StudentNotExistError()

    def update_student_by_id(self, student_id:int, data:dict) -> bool:
        try:
            student = Student.objects.get(id = student_id)
            for key,val in data.items():
                if val is not None:
                    setattr(student,key,val)
            student.save()
            return student
        
        except ObjectDoesNotExist:
            raise StudentNotExistError()
        except IntegrityError:
            raise StudentEmailError()
