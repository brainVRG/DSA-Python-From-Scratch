class LinkedList:
    def __init__(self):
        """Initializes an empty linked list with a null head pointer."""
        self.head = None

    def __iter__(self):
        """Yields each node in the linked list from head to tail using a generator."""
        current = self.head
        while current:
            yield current
            current = current.next
    

    # don't touch below this line

    def __repr__(self):
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):
            nodes.append(current.val)
            current = current.next
        return " -> ".join(nodes)
    
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val



# Updated test cases with character names from "The Hateful Eight"
run_cases = [
    ("John Ruth", ["Major Marquis Warren", "John Ruth"]),
    ("Daisy Domergue", ["Major Marquis Warren", "John Ruth", "Daisy Domergue"]),
    (
        "Chris Mannix",
        ["Major Marquis Warren", "John Ruth", "Daisy Domergue", "Chris Mannix"],
    ),
]

submit_cases = run_cases + [
    (
        "Bob",
        ["Major Marquis Warren", "John Ruth", "Daisy Domergue", "Chris Mannix", "Bob"],
    ),
    (
        "Oswaldo Mobray",
        [
            "Major Marquis Warren",
            "John Ruth",
            "Daisy Domergue",
            "Chris Mannix",
            "Bob",
            "Oswaldo Mobray",
        ],
    ),
]

def test(linked_list, input, expected_state):
    print("---------------------------------")
    print(f"Linked List: {linked_list}")
    print(f"Set Next: {input}")
    print(f"Expected: {expected_state}")
    node = Node(input)
    last_node = get_last_node(linked_list)
    last_node.set_next(node)
    try:
        result = linked_list_to_list(linked_list)
    except Exception as e:
        result = f"Error: {e}"
    print(f"Actual: {result}")
    if result == expected_state:
        print("Pass")
        return True
    print("Fail")
    return False

def linked_list_to_list(linked_list):
    result = []
    for node in linked_list:
        result.append(node.val)

    return result


def get_last_node(linked_list):
    current = linked_list.head
    while hasattr(current, "next") and current.next:
        current = current.next
    return current

def main():
    passed = 0
    failed = 0
    linked_list = LinkedList()
    linked_list.head = Node("Major Marquis Warren")
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(linked_list, *test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")

test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
