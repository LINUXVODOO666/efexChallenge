from abc import ABC, abstractmethod
from typing import List
from students.infrastructure.models import Student

# Abstract base class for student-related operations
class IStudents(ABC):
    
    # Method to get all students
    @abstractmethod
    def get_all_students(self) -> List[Student]:
        pass
    
    # Method to create a new student
    @abstractmethod
    def create_student(self, student: dict) -> Student:
        pass
    
    # Method to retrieve a student by their ID
    @abstractmethod
    def get_student_by_id(self, student_id: int) -> Student:
        pass
    
    # Method to update a student's data by their ID
    @abstractmethod
    def update_student_by_id(self, student_id: int, data: dict) -> Student:
        pass
