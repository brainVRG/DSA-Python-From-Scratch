class Stack:
    """A simple LIFO stack data structure."""
    
    def __init__(self):
        """Initializes an empty list to store stack items."""
        self.items = []

    def push(self, item):
        """Adds an item to the top of the stack."""
        self.items.append(item)

    def size(self):
        """Returns the current number of items in the stack."""
        return len(self.items)

    def peek(self):
        """Returns the top item without removing it, or None if empty in O(1) time."""
        return self.items[-1] if self.items else None

    def pop(self):
        """Removes and returns the top item, or None if empty in O(1) time."""
        return self.items.pop() if self.items else None