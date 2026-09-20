"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    student_grades = {}

    # Insert 5 key-value pairs into the hash table/dictionary.
    student_grades["Alice"] = 92
    student_grades["Bob"] = 85
    student_grades["Charlie"] = 78
    student_grades["Diana"] = 88
    student_grades["Evan"] = 95

    # Display the dictionary contents after insertion.
    print("Initial dictionary contents:", student_grades)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    # Lookup works by hashing the key and jumping to the stored value.
    # Since these keys exist, the lookups succeed.
    alice_grade = student_grades["Alice"]
    bob_grade = student_grades["Bob"]

    print(f"Alice's grade: {alice_grade}")
    print(f"Bob's grade: {bob_grade}")

    # If a key does not exist, Python raises a KeyError instead of returning
    # a value. This is demonstrated later in the edge cases section.

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    # Assigning a new value to an existing key updates that key's value.
    # It does not create a duplicate key; the dictionary size stays the same.
    print("Before update:", student_grades)

    student_grades["Alice"] = 97

    print("After updating Alice to 97:", student_grades)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    # The del statement removes the key-value pair from the dictionary.
    # Python hashes the key, finds the entry, and removes it.
    print("Before deletion:", student_grades)

    del student_grades["Charlie"]

    print("After deleting Charlie:", student_grades)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Added edge case 1:
    # Looking up a missing key raises a KeyError.
    print("Edge case 1: Looking up a missing key.")
    try:
        print(student_grades["Zoe"])
    except KeyError:
        print("KeyError: 'Zoe' is not in the dictionary.")

    # Explanation:
    # A normal dictionary lookup expects the key to exist. If it does not,
    # Python raises KeyError. This is useful for catching missing data.

    # Added edge case 2:
    # Deleting a missing key safely using pop() with a default value.
    print("Edge case 2: Deleting a missing key safely.")
    removed_value = student_grades.pop("Zoe", None)
    print(f"pop('Zoe', None) returned: {removed_value}")
    print("Dictionary after safe delete attempt:", student_grades)

    # Explanation:
    # pop(key, default) avoids a KeyError and returns the default value
    # when the key is not present.

    # Added edge case 3:
    # Assigning to a missing key inserts a new key-value pair.
    print("Edge case 3: Assigning to a missing key.")
    print("Before assigning 'Frank':", student_grades)

    student_grades["Frank"] = 90

    print("After assigning 'Frank':", student_grades)

    # Explanation:
    # Assigning to a key that does not exist adds a new entry to the
    # dictionary. This is how the hash table grows.

    # Added edge case 4:
    # Using get() on an empty dictionary avoids a KeyError.
    print("Edge case 4: Empty dictionary lookup with get().")
    empty_dict = {}
    print("get on empty dictionary:", empty_dict.get("missing", "default value"))

    # Explanation:
    # get() returns a default value instead of raising KeyError, making it
    # safe for optional lookups.

if __name__ == "__main__":
    main()