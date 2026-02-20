class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # O(n) - linear time
    # Same as Linked List
    def __repr__(self):
        if self.head is None:
            return "[]"
        else:
            last = self.head
            return_string = f"[{last.value}"

            while last.next:
                last = last.next
                return_string += f", {last.value}"
            
            return return_string+"]"
        
    # O(n) - linear time
    # Same as Linked List
    def __contains__(self, value):
        last = self.head
        while last is not None:
            if last.value == value:
                return True
            last = last.next
        return False

    # O(n) - linear time
    # Same as Linked List
    def __len__(self):
        last = self.head
        length = 0
        while last is not None:
            length += 1
            last = last.next
        return length

    # O(1) - constant time
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            last_node = Node(value)
            last_node.previous = self.tail
            self.tail.next = last_node
            self.tail = last_node

    # O(1) - constant time
    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            first_node = Node(value)
            first_node.next = self.head
            self.head.previous = first_node
            self.head = first_node

    # O(n) - linear time
    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
        else:
            if self.head is None:
                raise ValueError("Index out of bounds")
            else:
                last = self.head

                for i in range(index - 1):
                    if last.next is None:
                        raise ValueError("Index out of bounds")
                    else:
                        last = last.next

                adding_node = Node(value)
                adding_node.next = last.next
                adding_node.previous = last
                if last.next is not None:
                    last.next.previous = adding_node
                else:
                    self.tail = adding_node
                last.next = adding_node

    # O(n) - linear time        
    def delete(self, value):
        last = self.head

        if last is not None:
            if last.value == value:
                self.head = last.next
                if self.head is not None:
                    self.head.previous = None
                else:
                    self.tail = None
            else:
                while last.next:
                    if last.next.value == value:
                        if last.next.next is not None:
                            last.next.next.previous = last
                        else:
                            self.tail = last
                        last.next = last.next.next
                        break
                    last = last.next

    # O(n) - linear time
    def pop(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        elif index == 0:
            self.head = self.head.next
            if self.head is not None:
                self.head.previous = None
            else:
                self.tail = None
        else:
            last = self.head

            for i in range(index - 1):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next
            
            if last.next is None:
                raise ValueError("Index out of bounds")
            else:
                if last.next.next is not None:
                    last.next.next.previous = last
                else:
                    self.tail = last
                last.next = last.next.next

    # O(n) -linear time
    def get(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            last = self.head
            for i in range(index):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next
            return last.value
        
if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.append(10)
    dll.insert(5, 1)
    dll.insert(20, 1)
    dll.insert(18, 1)
    dll.insert(22, 1)
    dll.insert(88, 1)
    dll.insert(97, 1)


    dll.prepend(100)

    dll.insert(200, 1)

    dll.delete(18)
    dll.delete(22)
    dll.delete(5)

    dll.pop(1)

    print(dll)

    print(dll.get(1))

    print(29 in dll)

    print(800 in dll)