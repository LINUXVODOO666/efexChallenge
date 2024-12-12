import inject
from students.domain.interfaces import IStudents

# Action class to retrieve all students from the database
class GetAllStudents:
    @inject.autoparams() 
    def __init__(self, database: IStudents):
        self.db = database
        
    # Executes the action to fetch all students
    def execute(self):
        return self.db().get_all_students()

# Action class to create a new student in the database
class CreateStudent:
    @inject.autoparams() 
    def __init__(self, database: IStudents):
        self.db = database
        
    # Executes the action to create a new student
    def execute(self, student: dict):
        return self.db().create_student(student)

# Action class to retrieve a student by ID from the database
class GetStudentById:
    @inject.autoparams() 
    def __init__(self, database: IStudents):
        self.db = database
        
    # Executes the action to fetch a student by ID
    def execute(self, student_id: int):
        return self.db().get_student_by_id(student_id)

# Action class to update a student's data by ID in the database
class UpdateStudentById:
    @inject.autoparams() 
    def __init__(self, database: IStudents):
        self.db = database
        
    # Executes the action to update a student's data by ID
    def execute(self, student_id: int, data: dict):
        return self.db().update_student_by_id(student_id, data)

    