"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # If the tree is empty, the new value becomes the root.
        if self.root is None:
            self.root = Node(value)
        else:
            # Otherwise, recursively find the correct position.
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        if value < node.value:
            # If the left child is empty, insert here.
            if node.left is None:
                node.left = Node(value)
            else:
                # Otherwise, continue down the left subtree.
                self._insert_recursive(node.left, value)
        elif value > node.value:
            # If the right child is empty, insert here.
            if node.right is None:
                node.right = Node(value)
            else:
                # Otherwise, continue down the right subtree.
                self._insert_recursive(node.right, value)
        else:
            # Duplicate value = we ignore it.
            # Alternatively, we could store counts or allow duplicates in one subtree.
            pass

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is not None:
            # 1. Visit left subtree
            self._inorder_recursive(node.left, values)
            # 2. Visit current node
            values.append(node.value)
            # 3. Visit right subtree
            self._inorder_recursive(node.right, values)

def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    bst = BST()
    values_to_insert = [50, 30, 70, 20, 40, 60, 80]
    print(f"Inserting values: {values_to_insert}")
    for val in values_to_insert:
        bst.insert(val)
        # At each insertion, the tree compares the new value with nodes along
        # the path, halving the candidate subtree each time. This is why
        # insertion (and search) is O(log n) on average.
    print("Tree constructed successfully.")

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    sorted_values = bst.inorder()
    print(f"In‑order traversal result: {sorted_values}")
    # Explanation: In a BST, the left subtree always contains smaller values,
    # and the right subtree larger ones. Visiting left → node → right would
    # yield all values in non‑decreasing order.

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    # Existing values
    search_vals = [40, 80]
    for val in search_vals:
        found = bst.search(val)
        print(f"Search for {val}: {'Found' if found else 'Not found'}")
    # Non‑existing values
    search_vals_missing = [25, 100]
    for val in search_vals_missing:
        found = bst.search(val)
        print(f"Search for {val}: {'Found' if found else 'Not found'}")
    # Each search compares the target with the root, then moves left or right,
    # discarding half of the remaining tree at each step, leading to O(log n)
    # average performance.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")

    # 1. Empty tree traversal and search
    empty_bst = BST()
    print("Empty tree in‑order traversal:", empty_bst.inorder())
    print("Search in empty tree for 10:", empty_bst.search(10))
    # Both operations handle the empty root and return empty list / False.

    # 2. Duplicate insertion
    duplicate_val = 30
    bst.insert(duplicate_val)  # Should have no effect (duplicate ignored)
    print(f"After inserting duplicate {duplicate_val}, in‑order still sorted: {bst.inorder()}")

    # 3. Single‑node tree
    single_bst = BST()
    single_bst.insert(42)
    print("Single‑node tree in‑order:", single_bst.inorder())
    print("Search for 42 in single‑node:", single_bst.search(42))
    print("Search for 99 in single‑node:", single_bst.search(99))
    # The root is the only node, comparisons work as expected.

    # Additional note: In a severely unbalanced tree (e.g., inserting sorted
    # values), performance degrades to O(n).

if __name__ == "__main__":
    main()