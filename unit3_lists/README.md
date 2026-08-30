# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, I added this reflection to my initial discussion post in LEO.

### 1. What concepts or skills did you learn?

Completing this assignment really helped me understand what happens behind the scenes when we work with lists in Python. The biggest takeaway was how element shifting affects performance. I always knew that inserting at the beginning was slower, but actually seeing it explained with O(n) time complexity made it click. I also got better at writing defensive code like validating indexes before deletion to prevent crashes and makes functions more reliable.

### 2. What challenges did you encounter, and how did you overcome them?

One challenge was making sure my edge cases worked correctly. At first, I forgot to check if the index was an integer, so passing in a string would break the function. I fixed this by adding a type check along with the bounds check. I also had to think carefully about what to return when something goes wrong. I chose None for invalid deletions and -1 for missing values in the search function, which felt clean and avoided raising exceptions unnecessarily.

### 3. How do list operations impact performance in real-world applications?

These performance differences really matter in practice. For example, if you're building a social media feed where new posts are always added to the top, using an array‑based list could become slow as the feed grows because every new post shifts all existing posts down. A linked list would handle this much better since inserting at the front is O(1). On the other hand, if you're building a music player and mostly need to access songs by index, an array‑based list is perfect because random access is instant. Understanding these trade‑offs helps you choose the right data structure for the job which is something I'll definitely keep in mind for future projects.
