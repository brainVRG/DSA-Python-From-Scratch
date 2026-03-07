class Graph:
    def unconnected_vertices(self):
        """Finds and returns a list of all isolated vertices in the graph that have no connections."""
        result = []
        for node in self.graph.keys():
            if len(self.graph[node]) == 0:
                result.append(node)
        return result
    
    
    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = {v}
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = {u}

    def add_node(self, u):
        if u not in self.graph:
            self.graph[u] = set()

run_cases = [
    (
        [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
        ],
        [6, 7],
    ),
    (
        [
            (1, 2),
            (1, 3),
        ],
        [0, 4],
    ),
]
submit_cases = run_cases + [
    (
        [
            (0, 5),
            (7, 0),
        ],
        [1, 2, 3, 4],
    )
]



def test(edges_to_add, expected_vertices):
    print("=================================")
    graph = Graph()
    for edge in edges_to_add:
        graph.add_edge(edge[0], edge[1])
        print(f"Added edge: {edge}")
    for node in expected_vertices:
        graph.add_node(node)
        print(f"Added unconnected node: {node}")
    print("---------------------------------")
    try:
        unconnected = graph.unconnected_vertices()
        print(f" - Expecting: {expected_vertices}")
        print(f" - Actual: {unconnected}")
        if unconnected == expected_vertices:
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
