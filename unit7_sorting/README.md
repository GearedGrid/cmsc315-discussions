# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compares Bubble Sort and Merge Sort.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Test Bubble Sort and Merge Sort.
2. Use multiple datasets.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world sorting example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?

While doing this assignment, I learned how sorting works step by step. I practiced loops, swapping, recursion, dividing lists, and merging sorted halves. I also learned why edge cases like empty lists, duplicates, and already sorted lists matter.

2. What challenges did you encounter, and how did you overcome them?

My biggest challenge was merge sort, especially the merge function. Keeping track of the left and right indexes was confusing. I overcame it by tracing small examples on paper and testing tiny lists. Bubble sort was easier, but I had to remember the early-stop swap flag.

3. Compare and contrast each sorting algorithm based on efficiency differences, tradeoffs made, and when to each.

Comparing them, bubble sort is simple but slow, about O(n²), because it compares neighbors again and again. It uses little extra memory and is okay for very small or almost-sorted lists. Merge sort is faster on big lists, about O(n log n), because it splits the problem and merges efficiently. The tradeoff is that it uses extra memory and recursion. I would use bubble sort for learning or tiny data, and merge sort for larger data when speed matters and extra space is acceptable.