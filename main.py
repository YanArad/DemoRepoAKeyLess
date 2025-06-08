#!/usr/bin/env python3
"""
College Management System Demo

This script demonstrates the implementation of a simple college management system
with Student and College classes as specified in the requirements.

Requirements implemented:
1. Student class with properties: id, name, age, faculty
2. College class that stores a list of Student objects
3. College object filled with 3 Student objects
"""

from student import Student
from college import College


def main():
    """Main function to demonstrate the college management system."""
    print("=" * 60)
    print("College Management System Demo")
    print("=" * 60)
    
    # Create a College object
    my_college = College("AKeyLess University")
    print(f"\nCreated: {my_college}")
    
    # Create 3 Student objects as required
    student1 = Student(
        id=1001,
        name="Alice Johnson",
        age=20,
        faculty="Computer Science"
    )
    
    student2 = Student(
        id=1002,
        name="Bob Smith",
        age=22,
        faculty="Engineering"
    )
    
    student3 = Student(
        id=1003,
        name="Carol Williams",
        age=19,
        faculty="Computer Science"
    )
    
    # Add the students to the college
    print(f"\nAdding students to {my_college.name}:")
    print("-" * 40)
    my_college.add_student(student1)
    my_college.add_student(student2)
    my_college.add_student(student3)
    
    # Display all students
    my_college.display_all_students()
    
    # Display students grouped by faculty
    my_college.display_students_by_faculty()
    
    # Demonstrate additional functionality
    print(f"\nCollege Statistics:")
    print("-" * 40)
    print(f"Total students: {my_college.get_total_students()}")
    
    # Find students by faculty
    cs_students = my_college.get_students_by_faculty("Computer Science")
    print(f"Computer Science students: {len(cs_students)}")
    
    # Find a specific student
    found_student = my_college.get_student_by_id(1002)
    if found_student:
        print(f"\nFound student with ID 1002:")
        print(found_student.get_info())
    
    print(f"\nDemo completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()