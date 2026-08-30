"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Insert the value at the given index using the built-in insert method.
    # This shifts all elements from index to the right by one position,
    # increasing the list length by 1.
    # Performance: Inserting at the beginning (index 0) is O(n) because all
    # elements must be shifted right. Inserting at the end is O(1) amortized
    # (append). Inserting in the middle is O(n) on average because half the
    # elements are shifted.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Validate the index: it must be an integer and within the bounds of the list.
    # This prevents IndexError exceptions and ensures the function behaves predictably.
    # Safe deletion is important for robust code, especially when indices come from
    # user input or external sources. It avoids crashes and allows graceful error handling.
    if not isinstance(index, int):
        return None
    if index < 0 or index >= len(lst):
        return None
    # Pop the element at the index; this returns the removed value and shifts
    # all subsequent elements left by one position.
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # This is a linear search because we must examine each element in order
    # until we find a match or reach the end. In the worst case (value not present
    # or at the end), we scan all n elements. Hence O(n) time complexity.
    # Sequential scanning is necessary because the list is not sorted or indexed
    # by value; we have no other way to locate the element.
    for i, item in enumerate(lst):
        if item == value:
            return i
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    # Create a sample list
    my_list = [10, 20, 30, 40, 50]
    print("Original list:", my_list)

    # Insert at the beginning (index 0)
    insert_at(my_list, 0, 5)
    print("After inserting 5 at beginning:", my_list)
    # Explanation: All elements shifted right; now first element is 5.

    # Insert in the middle (index 3, which is after the first three elements)
    insert_at(my_list, 3, 25)
    print("After inserting 25 at index 3:", my_list)
    # Explanation: Elements from index 3 onward shifted right; 25 is now at position 3.

    # Insert at the end (index equal to current length)
    insert_at(my_list, len(my_list), 60)
    print("After inserting 60 at end:", my_list)
    # Explanation: Appending at the end; no shifting, O(1) amortized.

    # Reset list for subsequent tests
    my_list = [10, 20, 30, 40, 50]

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("Original list (reset):", my_list)

    # Delete from the beginning (index 0)
    removed = delete_at(my_list, 0)
    print(f"Removed value (beginning): {removed}")
    print("List after deletion:", my_list)
    # Explanation: Removed first element; all subsequent elements shifted left.

    # Delete from the middle (index 2, which is the third element in current list)
    removed = delete_at(my_list, 2)
    print(f"Removed value (middle): {removed}")
    print("List after deletion:", my_list)
    # Explanation: Removed element at index 2; elements after it shifted left.

    # Delete from the end (last index)
    removed = delete_at(my_list, len(my_list) - 1)
    print(f"Removed value (end): {removed}")
    print("List after deletion:", my_list)
    # Explanation: Removing the last element is O(1) as no shifting is needed.

    # Reset again for search and edge tests
    my_list = [10, 20, 30, 40, 50]

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("List:", my_list)

    # Search for an existing value
    target = 30
    idx = search_value(my_list, target)
    if idx != -1:
        print(f"Value {target} found at index {idx}")
    else:
        print(f"Value {target} not found")

    # Search for a non-existing value
    target = 99
    idx = search_value(my_list, target)
    if idx != -1:
        print(f"Value {target} found at index {idx}")
    else:
        print(f"Value {target} not found (returned -1)")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Edge case 1: Delete with invalid index (out of range)
    print("Edge case: Delete with invalid index (out of range)")
    invalid_index = 10
    removed = delete_at(my_list, invalid_index)
    print(f"Attempted delete at index {invalid_index}. Returned: {removed} (None)")
    # Explanation: The function validates the index and returns None, avoiding an exception.

    # Edge case 2: Delete from an empty list
    empty_list = []
    print("\nEdge case: Delete from an empty list")
    removed = delete_at(empty_list, 0)
    print(f"Attempted delete from empty list at index 0. Returned: {removed} (None)")
    # Explanation: The function checks index bounds and returns None safely.

    # Edge case 3: Insert into an empty list (works fine)
    print("\nEdge case: Insert into an empty list")
    insert_at(empty_list, 0, 100)
    print(f"After inserting 100 into empty list: {empty_list}")
    # Inserting at index 0 of an empty list is valid; the list becomes [100].


if __name__ == "__main__":
    main()