# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object‑oriented programming (OOP) in Python by building a simple **university registration‑style system**. The code defines a parent class (`Person`) and a child class (`Student`) to demonstrate inheritance, class/instance namespaces, and shallow vs. deep copying in a practical way.

---

## How the Structure and Logic Works

### 1. Inheritance Chain
- **`Person`** is the parent class. It has a class variable (`species = "Human"`), two instance variables (`name` and `age`), an `__init__` constructor, and a `display_info()` method that returns a formatted string: `"Name: <name>, Age: <age>"`.
- **`Student`** inherits from `Person` using `super().__init__()`. It adds:
  - A new class variable (`school = "University"`),
  - New instance variables (`student_id` and a list `courses`),
  - A new method (`add_course()`),
  - An **overridden** `display_info()` that calls the parent’s version and appends the student ID: `"Name: ..., Age: ..., ID: ..."`.

### 2. Namespace Demonstration (`demonstrate_namespaces()`)
- The function creates two `Student` objects (`student1` and `student2`).
- **Class namespace**: Accessing `Student.school` shows the class‑level variable shared by all instances.
- **Instance namespace**: Each object has its own `__dict__`. After creation, we add `graduation_year` **only** to `student1` – this new attribute appears only in `student1.__dict__`, proving that instance namespaces are isolated.
- The function prints both `__dict__` objects and the class namespace keys to make the distinction visible.

### 3. Shallow vs. Deep Copy (`demonstrate_copying()`)
- A helper class `Container` holds nested mutable data (a list containing another list).
- **Shallow copy** (`copy()`) duplicates the top‑level container but **shares** the inner list. When we modify the original’s inner list (`original.data[1].append(99)`), the shallow copy reflects that change.
- **Deep copy** (`deepcopy()`) recursively copies everything – the inner list is a **brand new** copy, so modifications to the original have no effect on the deep copy.
- The code prints all three objects and includes comments that clearly explain the difference.

---

## Real‑World Use Case

This code mirrors a **university student registration system**.
- The `Person` class holds basic info (name, age) for anyone in the system – students, staff, faculty.
- The `Student` subclass adds student‑specific data (ID, enrolled courses) and behaviors (adding a course).

**Why OOP makes sense here:**
- **Reusability** – common attributes (name, age) are defined once in `Person`; every subclass automatically gets them.
- **Maintainability** – if the university changes the ID format or wants to add a `birthdate`, you update only the `Person` or `Student` class, not every piece of code that uses them.
- **Extensibility** – you can later create `Professor` or `Staff` subclasses without breaking existing code.
- **Copy safety** – the deep‑copy demonstration is crucial when, for example, a registration office wants to create a temporary copy of a student’s record for editing (e.g., applying a scholarship) without altering the master database.

---

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object‑oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student‑created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.