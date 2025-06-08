class Student:
    """
    A class to represent a student in the college management system.
    
    Attributes:
        id (int): Unique identifier for the student
        name (str): Student's full name
        age (int): Student's age
        faculty (str): Faculty/Department the student belongs to
    """
    
    def __init__(self, id, name, age, faculty):
        """
        Initialize a new Student object.
        
        Args:
            id (int): Unique identifier for the student
            name (str): Student's full name
            age (int): Student's age
            faculty (str): Faculty/Department the student belongs to
        """
        self.id = id
        self.name = name
        self.age = age
        self.faculty = faculty
    
    def __str__(self):
        """Return a string representation of the student."""
        return f"Student(ID: {self.id}, Name: {self.name}, Age: {self.age}, Faculty: {self.faculty})"
    
    def __repr__(self):
        """Return a detailed string representation of the student."""
        return f"Student({self.id}, '{self.name}', {self.age}, '{self.faculty}')"
    
    def get_info(self):
        """Return a formatted string with student information."""
        return f"ID: {self.id}\nName: {self.name}\nAge: {self.age}\nFaculty: {self.faculty}"