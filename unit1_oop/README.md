# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object‑oriented programming (OOP) in Python through a practical vehicle‑fleet scenario. The code builds a parent class (`ParentClass` / `Vehicle`) and a child class (`ChildClass` / `Car`) to demonstrate how inheritance, class/instance namespaces, and object copying work in a realistic context.

## How the Structure and Logic Works

### 1. Inheritance Chain
- **ParentClass** defines a shared class variable (`category = "Vehicle"`), instance variables (`make`, `model`), an `__init__` constructor, and a basic `info()` method.
- **ChildClass** inherits from `ParentClass` using `super().__init__()`. It adds its own class variable (`type = "Car"`), new instance variables (`doors`, `fuel_type`), a new method (`honk()`), and **overrides** `info()` to include the child’s extra attributes while still reusing the parent’s logic.

### 2. Namespace Demonstration (`demonstrate_namespaces()`)
- **Class namespace** – class variables (e.g., `ChildClass.type`) are stored in the class’s `__dict__` and are shared by all instances.
- **Instance namespace** – each object has its own `__dict__` that stores instance‑specific data (e.g., `car1.make`).
- Adding `car1.color = "Red"` after creation modifies **only** `car1`’s instance namespace; `car2` remains unchanged, proving that instance namespaces are isolated.

### 3. Shallow vs. Deep Copy (`demonstrate_copying()`)
- A **shallow copy** (`copy()`) duplicates the top‑level container but shares nested mutable objects (like the inner list `[2, 3]`).  
  When the original’s inner list is modified (`original.data[1].append(99)`), the shallow copy reflects that change.
- A **deep copy** (`deepcopy()`) recursively duplicates everything, so the nested list in the copy is completely independent.  
  Modifications to the original do **not** affect the deep copy, ensuring full isolation.

---

## Real‑World Use Case

Imagine you are building a **fleet management system** for a car‑rental company.
- The `Vehicle` parent class represents the base entity – every vehicle has a `make` and `model`.
- The `Car` child class extends this with rental‑specific details, such as number of `doors` (for customer preferences) and `fuel_type` (to calculate refuelling costs).

This hierarchy lets you:
- Reuse core attributes (avoid code duplication).
- Override methods (e.g., a `calculate_rental_price()` method could behave differently for trucks vs. cars).
- Manage collections polymorphically – a list of `Vehicle` objects can safely include `Car`, `Truck`, or `Motorcycle` instances.

In practice, the namespace demonstration helps debug why certain shared settings (like a company‑wide `base_insurance_rate`) affect all vehicles unless overridden per instance. The copy demonstration is crucial when generating rental agreements: a **deep copy** of a vehicle object ensures that temporary edits (e.g., applying a discount) don’t accidentally alter the master inventory record.

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