"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    # Safety check: if the start node is not in the graph, return an empty list.
    # This prevents a KeyError and handles a missing start node safely.
    if start not in graph:
        return []

    # A queue is used because BFS must process nodes in first-in, first-out order.
    # This allows BFS to visit all nodes at the current level before moving deeper.
    queue = deque([start])

    # Track visited nodes so the same node is not added to the queue repeatedly.
    # Mark the start node as visited immediately.
    visited = {start}

    # This list stores the exact order in which nodes are visited.
    order = []

    while queue:
        # Remove the oldest node from the queue. This preserves level-by-level order.
        current = queue.popleft()
        order.append(current)

        # Add each unvisited neighbor to the queue.
        # Neighbors are queued so they are explored after the current level is processed.
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # BFS differs from depth-first traversal because BFS uses a queue and explores
    # all immediate neighbors before going deeper. DFS uses a stack or recursion and
    # follows one path as deeply as possible before backtracking.
    return order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    # This graph models a small social network or city route map.
    # Nodes represent people/cities: A, B, C, D, E, F, and G.
    # Edges represent direct connections between them.
    # The graph is undirected, so each connection appears in both nodes' adjacency lists.
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F", "G"],
        "F": ["C", "E"],
        "G": ["E"],
    }

    print("\n=== GRAPH STRUCTURE ===")
    print("TODO: Create and display a graph.")

    # Display the adjacency list so the graph structure is clear.
    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")
    print("TODO: Perform and explain BFS traversal.")

    # Select node A as the starting point.
    start = "A"

    # Perform BFS traversal.
    traversal = bfs(graph, start)
    print(f"BFS starting at {start}: {traversal}")

    # Explanation of level-by-level traversal:
    # Level 0: A
    # Level 1: B, C
    # Level 2: D, E, F
    # Level 3: G
    #
    # The queue makes BFS process A first, then all level-1 neighbors,
    # then all level-2 neighbors, and so on.
    print("Level-by-level explanation: A -> B,C -> D,E,F -> G")

    # Add a new edge to demonstrate an updated traversal.
    # Adding A--G creates a direct shortcut from the start node A to node G.
    graph["A"].append("G")
    graph["G"].append("A")

    updated_traversal = bfs(graph, start)
    print(f"After adding edge A--G, BFS starting at {start}: {updated_traversal}")

    # With A--G added, G is discovered immediately as a level-1 node
    # instead of being reached later through E.
    print("Updated level-by-level explanation: A -> B,C,G -> D,E,F")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge case 1: Start from a different node.
    # The graph is still connected, but the traversal order changes because
    # BFS expands outward from the new starting point.
    print("\nEdge Case 1: Starting from a different node (D)")
    traversal_from_d = bfs(graph, "D")
    print(f"BFS starting at D: {traversal_from_d}")
    print("Explanation: D starts at level 0, then B is level 1, then A/E are level 2, etc.")

    # Edge case 2: Missing start node.
    # If the requested start node is not in the graph, the function returns []
    # instead of raising an error.
    print("\nEdge Case 2: Missing start node (Z)")
    missing_traversal = bfs(graph, "Z")
    print(f"BFS starting at Z: {missing_traversal}")
    print("Explanation: Z is not a key in the adjacency list, so BFS safely returns no visited nodes.")

    # Edge case 3: Disconnected graph.
    # Here A/B and C/D form two separate components.
    # BFS only visits the component reachable from the chosen start node.
    disconnected_graph = {
        "A": ["B"],
        "B": ["A"],
        "C": ["D"],
        "D": ["C"],
    }

    print("\nEdge Case 3: Disconnected graph starting at A")
    disconnected_traversal = bfs(disconnected_graph, "A")
    print(f"BFS starting at A: {disconnected_traversal}")
    print("Explanation: Only A and B are reachable from A; C and D are in a separate component, so they are not visited.")

if __name__ == "__main__":
    main()