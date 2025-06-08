from student import Student
from typing import List, Optional


class College:
    """
    A class to represent a college that manages a collection of students.
    
    Attributes:
        name (str): Name of the college
        students (List[Student]): List of Student objects enrolled in the college
    """
    
    def __init__(self, name="Demo College"):
        """
        Initialize a new College object.
        
        Args:
            name (str): Name of the college (default: "Demo College")
        """
        self.name = name
        self.students = []
    
    def add_student(self, student):
        """
        Add a student to the college.
        
        Args:
            student (Student): Student object to add to the college
        """
        if isinstance(student, Student):
            # Check if student ID already exists
            if any(s.id == student.id for s in self.students):
                print(f"Warning: Student with ID {student.id} already exists!")
                return False
            self.students.append(student)
            print(f"Student {student.name} added successfully!")
            return True
        else:
            print("Error: Only Student objects can be added to the college!")
            return False
    
    def remove_student(self, student_id):
        """
        Remove a student from the college by ID.
        
        Args:
            student_id (int): ID of the student to remove
        
        Returns:
            bool: True if student was removed, False if not found
        """
        for i, student in enumerate(self.students):
            if student.id == student_id:
                removed_student = self.students.pop(i)
                print(f"Student {removed_student.name} removed successfully!")
                return True
        print(f"Student with ID {student_id} not found!")
        return False
    
    def get_student_by_id(self, student_id):
        """
        Find a student by their ID.
        
        Args:
            student_id (int): ID of the student to find
        
        Returns:
            Student or None: Student object if found, None otherwise
        """
        for student in self.students:
            if student.id == student_id:
                return student
        return None
    
    def get_students_by_faculty(self, faculty):
        """
        Get all students from a specific faculty.
        
        Args:
            faculty (str): Faculty name to filter by
        
        Returns:
            List[Student]: List of students in the specified faculty
        """
        return [student for student in self.students if student.faculty.lower() == faculty.lower()]
    
    def get_total_students(self):
        """
        Get the total number of students in the college.
        
        Returns:
            int: Number of students enrolled
        """
        return len(self.students)
    
    def display_all_students(self):
        """Display information of all students in the college."""
        if not self.students:
            print(f"{self.name} has no students enrolled.")
            return
        
        print(f"\n{self.name} - Student List:")
        print("=" * 50)
        for i, student in enumerate(self.students, 1):
            print(f"{i}. {student}")
    
    def display_students_by_faculty(self):
        """Display students grouped by faculty."""
        if not self.students:
            print(f"{self.name} has no students enrolled.")
            return
        
        # Group students by faculty
        faculties = {}
        for student in self.students:
            if student.faculty not in faculties:
                faculties[student.faculty] = []
            faculties[student.faculty].append(student)
        
        print(f"\n{self.name} - Students by Faculty:")
        print("=" * 50)
        for faculty, students in faculties.items():
            print(f"\n{faculty} Faculty ({len(students)} students):")
            for student in students:
                print(f"  - {student}")
    
    def __str__(self):
        """Return a string representation of the college."""
        return f"College: {self.name} ({self.get_total_students()} students)"
    
    def __repr__(self):
        """Return a detailed string representation of the college."""
        return f"College('{self.name}', {self.get_total_students()} students)"