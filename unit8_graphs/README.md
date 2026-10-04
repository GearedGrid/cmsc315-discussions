# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explores graph traversal using Breadth-First Search (BFS).

## Learning Objectives

- Represent graphs using adjacency lists
- Implement BFS
- Use queues in graph traversal
- Analyze graph traversal behavior

## Requirements

1. Create a graph.
2. Perform BFS traversal.
3. Add nodes or edges.
4. Demonstrate edge cases.
5. Analyze BFS behavior.
6. Create a real-world graph example.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?

While completing this assignment, I learned how BFS moves through a graph level by level using a queue. I also practiced tracking visited nodes so the same node does not get processed twice.

2. What challenges did you encounter, and how did you overcome them?

The biggest challenge was understanding why the queue order matters and how to handle edge cases, like a missing start node or a disconnected graph. I overcame this by tracing small examples on paper and testing different starting nodes.

3. Compare BFS and DFS conceptually and describe real-world applications and use cases.

Comparing BFS and DFS, BFS explores all nearby nodes first and uses a queue, while DFS goes as deep as possible down one path and uses a stack or recursion. BFS is useful when I want the shortest path in an unweighted graph, such as finding the fewest friend connections between people or the shortest route with equal-cost stops. DFS is better for exploring all possibilities, like solving a maze, checking cycles, or searching deeply through file folders.

Overall, this assignment helped me see how graph traversal connects to real computer science problems.