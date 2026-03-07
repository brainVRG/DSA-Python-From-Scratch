class Graph:
    def __init__(self):
        """Initializes an empty dictionary to store the graph's adjacency list."""
        self.graph = {}

    def add_edge(self, u, v):
        """Adds an undirected edge between vertices u and v, creating their sets if they do not exist."""
        if u not in self.graph:
            self.graph[u] = set()
        if v not in self.graph:
            self.graph[v] = set()
        self.graph[u].add(v)
        self.graph[v].add(u)


    # don't touch below this line

    def edge_exists(self, u, v):
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) and (u in self.graph[v])
        return False
    
    
run_cases = [
    (
        [
            (0, 1),
            (2, 0),
        ],
        (
            [
                (1, 0),
                (1, 2),
                (2, 0),
            ],
            [True, False, True],
        ),
    ),
    (
        [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
        ],
        (
            [
                (0, 1),
                (1, 2),
                (0, 4),
                (2, 5),
                (5, 0),
            ],
            [True, True, False, False, False],
        ),
    ),
]
submit_cases = run_cases + [
    (
        [
            (0, 1),
            (2, 4),
            (2, 1),
            (3, 1),
            (4, 5),
        ],
        (
            [
                (5, 4),
                (1, 5),
                (0, 4),
                (2, 5),
                (1, 3),
            ],
            [True, False, False, False, True],
        ),
    ),
]


def test(edges_to_add, edges_to_check):
    print("=================================")
    graph = Graph()
    for edge in edges_to_add:
        graph.add_edge(edge[0], edge[1])
        print(f"Added edge: {edge}")
    print("---------------------------------")
    try:
        actual = []
        for i, edge in enumerate(edges_to_check[0]):
            exists = graph.edge_exists(edge[0], edge[1])
            actual.append(exists)
            print(f"{edge} exists:")
            print(f" - Expecting: {edges_to_check[1][i]}")
            print(f" - Actual: {exists}")
        if actual == edges_to_check[1]:
            print("Pass \n")
            return True
        print("Fail \n")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
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