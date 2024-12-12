from abc import ABC, abstractmethod
from typing import List 
from students.infrastructure.models import Student


class IStudents(ABC):
    @abstractmethod
    def get_all_students(self) -> List[Student]:
        pass
