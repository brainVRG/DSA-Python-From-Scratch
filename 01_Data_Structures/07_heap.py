class MinHeap:

    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def __repr__(self):
        return str(self.heap)

    # O(log n)
    def insert(self, key, value):
        self.heap.append((key, value))
        self._sift_up(len(self.heap) - 1)

    # O(1)
    def peek_min(self):
        if not self.heap:
            raise IndexError("Empty Heap")

        return self.heap[0]

    # O(log n)
    def extract_min(self):
        if not self.heap:
            raise IndexError("Empty Heap")

        min_element = self.heap[0]
        last_element = self.heap.pop()

        if self.heap:
            self.heap[0] = last_element
            self._sift_down(0)
        
        return min_element
    
    # O(n)
    def heapify(self, elements):
        self.heap = list(elements)

        for i in range(len(self.heap) // 2 -1, -1, -1):
            self._sift_down(i)

    # O(n)
    def meld(self, other_heap):
        combined_heap = self.heap + other_heap.heap
        self.heapify(combined_heap)

        other_heap.heap = []

    # o(1)
    def _parent(self, index):
        return (index - 1) // 2 if index != 0 else None

    # o(1)
    def _left(self, index):
        left = 2 * index + 1
        return left if left < len(self.heap) else None

    # o(1)
    def _right(self, index):
        right = 2 * index + 2
        return right if right < len(self.heap) else None
    
    # o(log n)
    def _sift_up(self, index): # swim
        parent_index = self._parent(index)
        
        while parent_index is not None and self.heap[index][0] < self.heap[parent_index][0]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = self._parent(index)

    # o(log n)
    def _sift_down(self, index): # sink
        while True:
            smallest = index

            left = self._left(index)
            right = self._right(index)

            if left is not None and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left

            if right is not None and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

if __name__ == '__main__':
    min_heap = MinHeap()
    min_heap.heapify([(10, '0'), (9, '0'), (8, '0'), (7, '0'), (6, '0'), (5, '0'), (4, '0'), (3, '0'), (2, '0'), (1, '0')])
    print(min_heap)

    import heapq
    mylist = [(10, '0'), (9, '0'), (8, '0'), (7, '0'), (6, '0'), (5, '0'), (4, '0'), (3, '0'), (2, '0'), (1, '0')]
    heapq.heapify(mylist)
    print(mylist)

    print(min_heap.extract_min())
    print(min_heap.extract_min())
    print(min_heap.extract_min())
    
    print(heapq.heappop(mylist))
    print(heapq.heappop(mylist))
    print(heapq.heappop(mylist))

    min_heap.insert(2, '2')
    print(min_heap)

    heapq.heappush(mylist, (2, '2'))
    print(mylist)

    min_heap2 = MinHeap()
    min_heap2.heapify([(5, '5'), (7, '7'), (2, '2')])
    min_heap.meld(min_heap2)
    print(min_heap)