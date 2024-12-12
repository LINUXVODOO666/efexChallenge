class StudentEmailError(Exception):
    def __init__(self, message="Email already exists"):
        self.message = message
        super().__init__(self.message)
        
        
class StudentNotExistError(Exception):
    def __init__(self, message="Student not exist"):
        self.message = message
        super().__init__(self.message)