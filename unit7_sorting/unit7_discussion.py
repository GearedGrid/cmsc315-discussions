"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    sorted_lst = lst[:]
    n = len(sorted_lst)

    # Traverse through all elements in the list
    for i in range(n):
        swapped = False

        # Last i elements are already in their correct sorted position
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if sorted_lst[j] > sorted_lst[j + 1]:
                # Swap if they are out of order
                sorted_lst[j], sorted_lst[j + 1] = sorted_lst[j + 1], sorted_lst[j]
                swapped = True

        # If no swaps occurred, the list is already sorted
        if not swapped:
            break

    return sorted_lst


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # Base case: a list with 0 or 1 element is already sorted
    if len(lst) <= 1:
        return lst[:]

    # Find the middle point and divide the list into two halves
    mid = len(lst) // 2
    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])

    # Merge the two sorted halves together
    return merge(left_half, right_half)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    # Result list for the merged sorted values
    result = []
    i = 0
    j = 0

    # Compare values from left and right until one list is exhausted
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining values from the left list
    result.extend(left[i:])

    # Append any remaining values from the right list
    result.extend(right[j:])

    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    print("TODO: Create an unsorted dataset and test both sorting algorithms.")

    # Dataset #1: at least 7 unsorted values
    dataset1 = [42, 17, 93, 8, 23, 55, 4, 71]

    print("Original Dataset #1:", dataset1)
    print("Bubble Sort Result:", bubble_sort(dataset1))
    print("Merge Sort Result: ", merge_sort(dataset1))

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    print("TODO: Create a second dataset and compare sorting results.")

    # Dataset #2: different values, including duplicates and negative numbers
    dataset2 = [30, -5, 12, 30, 7, 0, 19, -2]

    bubble_result2 = bubble_sort(dataset2)
    merge_result2 = merge_sort(dataset2)

    print("Original Dataset #2:", dataset2)
    print("Bubble Sort Result:", bubble_result2)
    print("Merge Sort Result: ", merge_result2)
    print("Comparison: Both algorithms produced the same sorted result:", bubble_result2 == merge_result2)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")


    # Edge Case 1: List with duplicate values
    print("\n--- Edge Case 1: Duplicate Values ---")
    duplicates = [4, 2, 4, 1, 2, 4]
    print("Original:", duplicates)
    print("Bubble Sort:", bubble_sort(duplicates))
    print("Merge Sort: ", merge_sort(duplicates))
    print("Explanation: Both algorithms keep duplicate values. The duplicates appear multiple times in the sorted output.")

    # Edge Case 2: Single-element list
    print("\n--- Edge Case 2: Single-Element List ---")
    single_element = [99]
    print("Original:", single_element)
    print("Bubble Sort:", bubble_sort(single_element))
    print("Merge Sort: ", merge_sort(single_element))
    print("Explanation: A single-element list is already sorted, so both algorithms return it unchanged.")


if __name__ == "__main__":
    main()