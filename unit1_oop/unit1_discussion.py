"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class Person:
    # Class variable
    species = "Human"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    # Method that returns information about the object
    def display_info(self):
        return "Name: " + str(self.name) + ", Age: " + str(self.age)


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class Student(Person):
    # New class variable
    school = "University"

    def __init__(self, name, age, student_id, courses=None):
        # Call parent constructor
        super().__init__(name, age)
        # New instance variables
        self.student_id = student_id
        # Use a new list for each instance to avoid sharing
        self.courses = courses.copy() if courses else []

    # New method
    def add_course(self, course):
        self.courses.append(course)

    # Override parent method
    def display_info(self):
        base = super().display_info()
        return base + ", ID: " + str(self.student_id)


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    # Create two student objects
    student1 = Student("Alice", 30, "S001", ["Math", "Physics"])
    student2 = Student("Bob", 22, "S002", ["History"])

    # Access class variable through class itself
    print("Class variable via class (Student.school):", Student.school)

    # Access class variable through an object
    print("Class variable via object (student1.school):", student1.school)

    # Add a new attribute to only one object after creation
    student1.graduation_year = 2026

    # Display each object's namespace using __dict__
    print("\nstudent1.__dict__:", student1.__dict__)
    print("student2.__dict__:", student2.__dict__)

    # Display information about the class namespace
    print("\nClass namespace (Student.__dict__ keys):", list(Student.__dict__.keys()))
    # Specifically show class variables
    print("Class variables:", Student.species, Student.school)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    # Create an object with nested mutable data
    class Container:
        def __init__(self, data):
            self.data = data

        def __repr__(self):
            return f"Container({self.data})"

    original = Container([1, [2, 3], 4])

    # Shallow copy
    shallow = copy(original)

    # Deep copy
    deep = deepcopy(original)

    # Modify the original's nested data (append to the inner list)
    original.data[1].append(99)

    # Display all
    print("Original after modification:", original)
    print("Shallow copy:", shallow)
    print("Deep copy:", deep)

    # Shallow copy: The outer container is copied, but inner objects (the inner list) are shared.
    # Modifying the nested list in the original also affects the shallow copy because they reference the same inner list.

    # Deep copy: All objects are recursively copied.
    # The inner list is a separate copy, so modifications to the original's nested list do not affect the deep copy.


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nCreating and testing Person object")
    person = Person("John", 22)
    print("Person info:", person.display_info())

    print("\nCreating and testing Student object")
    student = Student("Alice", 30, "S123", ["CS101", "MATH202"])
    print("Student info:", student.display_info())
    student.add_course("PHY101")
    print("Student courses after adding:", student.courses)

    # Call demonstration functions
    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()