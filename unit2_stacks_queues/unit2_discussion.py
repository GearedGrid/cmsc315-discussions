"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # Internal storage: a Python list. The end of the list represents the top of the stack.
        self.items = []

    def push(self, value):
        # Add value to the top (end) of the list.
        # LIFO: the last element appended will be the first one removed.
        self.items.append(value)

    def pop(self):
        # Remove and return the top (last) element.
        # If the stack is empty, raise an IndexError with a clear message.
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        # Return the top value without removing it.
        # Useful for inspecting the most recent item without altering the stack.
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        # Return True if the stack contains no elements.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # Use deque from collections for efficient O(1) appends and poplefts.
        self.items = deque()

    def enqueue(self, value):
        # Add value to the back (right end) of the deque.
        # FIFO: the first element added will be the first one removed.
        self.items.append(value)

    def dequeue(self):
        # Remove and return the front (leftmost) element.
        # If the queue is empty, raise an IndexError with a clear message.
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.popleft()

    def front(self):
        # Return the front value without removing it.
        # Useful for examining the next element to be dequeued.
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.items[0]

    def is_empty(self):
        # Return True if the queue contains no elements.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===\n")

    # ===============================
    # STACK DEMO
    # ===============================
    print("--- STACK DEMO (LIFO) ---")
    stack = Stack()

    # 1. Add at least 4 values.
    print("Pushing values: 10, 20, 30, 40")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)

    # 2. Demonstrate LIFO behavior.
    print("Stack contents (top to bottom):", stack.items[::-1])  # show top first
    print("Peek at top:", stack.peek())
    print("Pop once:", stack.pop())
    print("Pop again:", stack.pop())
    print("After two pops, stack (top to bottom):", stack.items[::-1])

    # 3. Show what happens when pop() is used on an empty stack.
    print("\nTesting empty-stack pop:")
    # Empty the stack completely.
    while not stack.is_empty():
        stack.pop()
    try:
        stack.pop()
    except IndexError as e:
        print("Caught expected error:", e)

    # 4. Test peek() on an empty stack.
    print("\nTesting empty-stack peek:")
    try:
        stack.peek()
    except IndexError as e:
        print("Caught expected error:", e)

    # 5. Single-item stack: add one, remove it, verify empty.
    print("\nSingle-item stack test:")
    stack.push(99)
    print("Stack after pushing 99 (top to bottom):", stack.items[::-1])
    removed = stack.pop()
    print(f"Popped: {removed}, stack is empty? {stack.is_empty()}")

    # ===============================
    # QUEUE DEMO
    # ===============================
    print("\n--- QUEUE DEMO (FIFO) ---")
    queue = Queue()

    # 1. Add at least 4 values.
    print("Enqueuing values: 'A', 'B', 'C', 'D'")
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    queue.enqueue('D')

    # 2. Demonstrate FIFO behavior.
    print("Queue contents (front to back):", list(queue.items))
    print("Front element:", queue.front())
    print("Dequeue once:", queue.dequeue())
    print("Dequeue once:", queue.dequeue())
    print("After two dequeues, queue (front to back):", list(queue.items))

    # 3. Show what happens when dequeue() is used on an empty queue.
    print("\nTesting empty-queue dequeue:")
    while not queue.is_empty():
        queue.dequeue()
    try:
        queue.dequeue()
    except IndexError as e:
        print("Caught expected error:", e)

    # 4. Test front() on an empty queue.
    print("\nTesting empty-queue front:")
    try:
        queue.front()
    except IndexError as e:
        print("Caught expected error:", e)

    # 5. Single-item queue: add one, remove it, verify empty.
    print("\nSingle-item queue test:")
    queue.enqueue('Z')
    print("Queue after enqueuing 'Z' (front to back):", list(queue.items))
    removed = queue.dequeue()
    print(f"Dequeued: {removed}, queue is empty? {queue.is_empty()}")


if __name__ == "__main__":
    main()