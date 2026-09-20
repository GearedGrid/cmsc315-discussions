# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?

While completing this assignment, I learned how Python dictionaries function like hash tables. I practiced inserting, looking up, updating, and deleting key-value pairs, and I saw how quickly these operations work when keys are unique and hashable.

2. What challenges did you encounter, and how did you overcome them?

One challenge was understanding how to handle missing keys without crashing the program. I overcame this by using try/except blocks and the pop() and get() methods with default values. These techniques made my code more robust.

3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.

Hash tables behave by hashing each key into an index, which allows the computer to jump almost directly to the associated value instead of searching through every item. Collisions occur when two different keys hash to the same index. Python handles collisions internally, so the dictionary still works correctly. Because of this design, hash tables provide average O(1) lookup, insertion, and deletion time. That efficiency makes them useful for real-world tasks like gradebooks, caches, and databases. Overall, this assignment strengthened my understanding of both Python dictionaries and hash table efficiency.