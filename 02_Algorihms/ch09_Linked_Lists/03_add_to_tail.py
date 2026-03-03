class LinkedList:
    def add_to_tail(self, node):
        """Appends a new node to the tail of the linked list in O(N) time."""
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node

    # don't touch below this line

    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val

run_cases = [
    (["Major Marquis Warren", "John Ruth"],),
    (["Major Marquis Warren", "John Ruth", "Daisy Domergue"],),
]

submit_cases = run_cases + [
    (["Major Marquis Warren", "John Ruth", "Daisy Domergue", "Chris Mannix"],),
    (["Major Marquis Warren", "John Ruth", "Daisy Domergue", "Chris Mannix", "Bob"],),
    (
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


def test(inputs):
    print("---------------------------------")
    linked_list = LinkedList()
    for val in inputs:
        linked_list.add_to_tail(Node(val))
    actual = linked_list_to_list(linked_list)

    print(f"Expected: {inputs}")
    print(f"Actual  : {actual}")

    if actual == inputs:
        print("Pass")
        return True
    else:
        print("Fail")
        return False


def linked_list_to_list(linked_list):
    return [node.val for node in linked_list]


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        if test(test_case[0]):
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
