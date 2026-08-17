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

class ParentClass:
    # Class variable
    category = "Vehicle"

    def __init__(self, make, model):
        #Instance variables
        self.make = make
        self.model = model

    # Method that returns information about the object
    def info(self):
        return f"{self.make} {self.model}"


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

class ChildClass(ParentClass):
    # New class variable
    type = "Car"

    def __init__(self, make, model, doors, fuel_type):
        # Call parent constructor
        super().__init__(make, model)
        # New instance variables
        self.doors = doors
        self.fuel_type = fuel_type

    # New method
    def honk(self):
        return "Beep beep!"

    # Override parent method
    def info(self):
        return f"{super().info()} (Doors: {self.doors}, Fuel: {self.fuel_type})"


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
    print("TODO: Implement namespace demonstration")

    # Create two child objects
    car1 = ChildClass("Toyota", "Corolla", 4, "Petrol")
    car2 = ChildClass("Tesla", "Model 3", 4, "Electric")

    # Access class variable through class itself
    print("Class variable via class (ChildClass.type):", ChildClass.type)

    # Access class variable through an object
    print("Class variable via object (car1.type):", car1.type)

    # Add a new attribute to only one object after creation
    car1.color = "Black"

    # Display each object's namespace using __dict__
    print("\ncar1.__dict__:", car1.__dict__)
    print("car2.__dict__:", car2.__dict__)

    # Display information about the class namespace
    print("\nClass namespace (ChildClass.__dict__ keys):", list(ChildClass.__dict__.keys()))
    # Specifically show class variables
    print("Class variables:", ChildClass.type, ChildClass.category)


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
    print("TODO: Implement shallow copy and deep copy demonstration")

    # Create an object with nested mutable data
    class Container:
        def __init__(self, data):
            self.data = data

        def __repr__(self):
            return f"Container({self.data})"

    original = Container([1, [2, 3], 4])

    # Shallow copy
    shallow = copy (original)

    # Deep copy
    deep = deepcopy (original)

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

    print("\nTODO: Create and test your parent object")
    parent_obj = ParentClass("Generic", "Vehicle")
    print("\nParent object info:", parent_obj.info())

    print("\nTODO: Create and test your child object")
    child_obj = ChildClass("Honda", "Civic", 4, "Hybrid")
    print("Child object info:", child_obj.info())
    print("Child object honk:", child_obj.honk())

    # Call demonstration functions
    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()