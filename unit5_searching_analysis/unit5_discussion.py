"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""

import time

def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Implementation added:
    # Linear search checks each element in order.
    # Worst case: the target is the last element or is not present,
    # so the loop must check all n elements.
    # Each additional element adds at most one more comparison.
    # Therefore, the time complexity is O(n).
    for index in range(len(lst)):
        if lst[index] == target:
            return index

    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # Implementation added:
    # Binary search requires the list to be sorted.
    left = 0
    right = len(lst) - 1

    while left <= right:
        # Find the middle of the current search interval.
        mid = left + (right - left) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            # The middle value is too small, so the target must be
            # in the right half. Discard the left half.
            left = mid + 1
        else:
            # The middle value is too large, so the target must be
            # in the left half. Discard the right half.
            right = mid - 1

    # Target was never found.
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")

    # Implementation added:
    small_data = [3, 7, 12, 19, 25, 31, 42, 56, 68, 74]
    existing_value = 31
    missing_value = 100

    print("Small sorted dataset:", small_data)

    print(f"Searching for existing value {existing_value}:")
    print("  Linear search result:", linear_search(small_data, existing_value))
    print("  Binary search result:", binary_search(small_data, existing_value))

    print(f"Searching for missing value {missing_value}:")
    print("  Linear search result:", linear_search(small_data, missing_value))
    print("  Binary search result:", binary_search(small_data, missing_value))

    # Explanation:
    # Both algorithms find 31 at index 5.
    # Both return -1 for 100 because it is not in the list.
    # On a small list, the difference in performance is not very noticeable,
    # but binary search works correctly because the list is sorted.

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")

    # Implementation added:
    large_data = list(range(100_000))
    large_existing = 99_999
    large_missing = -1

    start = time.perf_counter()
    linear_existing_result = linear_search(large_data, large_existing)
    linear_existing_time = time.perf_counter() - start

    start = time.perf_counter()
    binary_existing_result = binary_search(large_data, large_existing)
    binary_existing_time = time.perf_counter() - start

    start = time.perf_counter()
    linear_missing_result = linear_search(large_data, large_missing)
    linear_missing_time = time.perf_counter() - start

    start = time.perf_counter()
    binary_missing_result = binary_search(large_data, large_missing)
    binary_missing_time = time.perf_counter() - start

    print("Large sorted dataset size:", len(large_data))

    print(f"Searching for existing value {large_existing} at the end:")
    print(f"  Linear search: index {linear_existing_result}, time {linear_existing_time:.8f}s")
    print(f"  Binary search: index {binary_existing_result}, time {binary_existing_time:.8f}s")

    print(f"Searching for missing value {large_missing}:")
    print(f"  Linear search: index {linear_missing_result}, time {linear_missing_time:.8f}s")
    print(f"  Binary search: index {binary_missing_result}, time {binary_missing_time:.8f}s")

    # Explanation:
    # Linear search must scan many elements, so its time grows directly with n.
    # Binary search cuts the remaining search space in half each iteration.
    # For 100,000 items, binary search needs only about 17 comparisons,
    # while linear search may need up to 100,000 comparisons.
    # This is why binary search becomes much more efficient on large sorted datasets.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Implementation added:
    empty_list = []
    print("Edge case 1 - empty list:")
    print("  linear_search([], 5):", linear_search(empty_list, 5))
    print("  binary_search([], 5):", binary_search(empty_list, 5))
    print("  Explanation: there are no elements to check, so both return -1 immediately.")

    single_list = [42]
    print("Edge case 2 - single-element list [42]:")
    print("  linear_search([42], 42):", linear_search(single_list, 42))
    print("  binary_search([42], 42):", binary_search(single_list, 42))
    print("  linear_search([42], 7):", linear_search(single_list, 7))
    print("  binary_search([42], 7):", binary_search(single_list, 7))
    print("  Explanation: when the target exists, index 0 is returned.")
    print("  When the target is missing, both return -1.")

    first_last_list = [10, 20, 30, 40, 50]
    print("Edge case 3 - target at first and last positions:")
    print(
        "  first value 10 -> linear:",
        linear_search(first_last_list, 10),
        "binary:",
        binary_search(first_last_list, 10)
    )
    print(
        "  last value 50 -> linear:",
        linear_search(first_last_list, 50),
        "binary:",
        binary_search(first_last_list, 50)
    )
    print("  Explanation: linear search finds the first value quickly but may")
    print("  take longer for the last value. Binary search handles both efficiently")
    print("  because it uses the sorted order to reduce the search space.")


if __name__ == "__main__":
    main()