import inject

from students.domain.interfaces import IStudents

class GetAllStudents:
    @inject.autoparams()
    def __init__(self,database:IStudents):
        self.db = database
        
    def execute(self):
        return self.db().get_all_students()
    
class CreateStudent:
    @inject.autoparams()
    def __init__(self,database:IStudents):
        self.db = database
        
    def execute(self, student:dict):
        return self.db().create_student(student)
    
class GetStudentById:
    @inject.autoparams()
    def __init__(self,database:IStudents):
        self.db = database
        
    def execute(self, student_id:int):
        return self.db().get_student_by_id(student_id)
    
class UpdateStudentById:
    @inject.autoparams()
    def __init__(self,database:IStudents):
        self.db = database
        
    def execute(self, student_id:int,data:dict):
        return self.db().update_student_by_id(student_id,data)
    
    