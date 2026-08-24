# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Implementation Approach

- Data Storage Choices
    - The Stack uses a standard Python list, treating the end of the list as the top. This makes push (.append()), pop (.pop()), and peek ([-1]) both simple and efficient (O(1)).
    - The Queue uses collections.deque instead of a list, because deque provides O(1) performance for appends (.append()) on the right and pops (.popleft()) from the left—exactly what a FIFO queue needs.

- Error Handling  
  Rather than printing messages or returning None when a structure is empty, the pop, peek, dequeue, and front methods raise IndexError with explicit, descriptive messages (e.g., "pop from empty stack"). This follows Python’s common “ask forgiveness, not permission” philosophy and makes debugging straightforward.

- Demonstration & Testing  
  All demo logic is placed inside the main() function, providing a clear, step‑by‑step walkthrough:
    - Each operation (push/enqueue, pop/dequeue, peek/front) is accompanied by print statements that show the internal state (top‑to‑bottom for stacks, front‑to‑back for queues) before and after changes.
    - LIFO and FIFO ordering are explicitly verified by adding multiple items and removing them in sequence.
    - Edge cases are thoroughly tested using try/except blocks that gracefully catch the expected IndexError when operations are performed on empty structures.
    - A dedicated single‑item test confirms that after adding and removing one element, the is_empty() method correctly returns True.

- Code Documentation  
  Every method includes a clear, concise comment that explains:
    - What the method does.
    - Why the operation supports LIFO or FIFO behavior.
    - What happens in edge cases (empty stack/queue).

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.