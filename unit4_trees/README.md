# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

## Discussion Board Reflection

### 1. What concepts or skills did you learn?

After completing the programming assignment, I gained a much deeper understanding of how recursive tree operations work and why the BST property (left < node < right) is so powerful. The most valuable skill I learned was tracing recursive calls through the tree, especially when inserting or searching—it helped me visualise how the stack unwinds and how each subtree is handled independently.

### 2. What challenges did you encounter, and how did you overcome them?

I encountered two main challenges: handling duplicate insertions gracefully and ensuring the recursive search worked on an empty tree. I solved the first by explicitly checking for equality and doing nothing (ignoring duplicates), which kept the tree simple and predictable. For the second, I added a base case at the start of each recursive method to return immediately when a "None" node is reached.

### 3. How do list operations impact performance in real-world applications?

The BST's ordering is what creates its efficiency. Unlike an unsorted array or linked list, where we must scan every element (O(n)) to find a value, a BST halves the search space at each step by comparing the target with the current node and moving left or right. This gives average‑case O(log n) performance—comparable to binary search on a sorted array, but with the added benefit of dynamic insertions and deletions without shifting elements. The in‑order traversal further showcases this ordering by producing a sorted list, proving that the tree's structure inherently encodes a sorted sequence.