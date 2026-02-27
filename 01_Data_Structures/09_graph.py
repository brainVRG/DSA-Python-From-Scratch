class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = dict()

    def __repr__(self):
        graph_str = ""
        for node, neighbors in self.adj_list.items():
            graph_str += f"{node} -> {neighbors}\n"
        return graph_str

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:   
            raise ValueError(f'Node {node} already exists')

    def remove_node(self, node):
        if node not in self.adj_list:
            raise ValueError(f'Node {node} does not exist')
        
        for neighbors in self.adj_list.values():
            items_to_remove = [x for x in neighbors if x == node or (isinstance(x, tuple) and x[0] == node)]
            for item in items_to_remove:
                neighbors.remove(item)
        
        del self.adj_list[node]

    def add_edge(self, from_node, to_node, weight=None):
        if from_node not in self.adj_list:
            self.add_node(from_node)
        if to_node not in self.adj_list:
            self.add_node(to_node)

        if weight is None:
            self.adj_list[from_node].add(to_node)
            if not self.directed:
                self.adj_list[to_node].add(from_node)
        else:
            self.adj_list[from_node].add((to_node, weight))
            if not self.directed:
                self.adj_list[to_node].add((from_node, weight))

    def remove_edge(self, from_node, to_node):
        if from_node not in self.adj_list or to_node not in self.adj_list:
            raise ValueError("Node does not exist")

        def _remove_target(source, target):
            target_item = next((x for x in self.adj_list[source] if x == target or (isinstance(x, tuple) and x[0] == target)), None)
            if target_item is not None:
                self.adj_list[source].remove(target_item)
            else:
                raise ValueError(f"Edge from {source} to {target} does not exist")

        _remove_target(from_node, to_node)
        if not self.directed:
            _remove_target(to_node, from_node)
        
    def get_neighbors(self, node):
        return self.adj_list.get(node, set())

    def has_node(self, node):
        return node in self.adj_list

    def has_edge(self, from_node, to_node):
        if from_node in self.adj_list:
            return any(x == to_node or (isinstance(x, tuple) and x[0] == to_node) for x in self.adj_list[from_node])
        return False

    def get_nodes(self):
        return list(self.adj_list.keys())

    def get_edges(self):
        edges = []
        for from_node, neighbors in self.adj_list.items():
            for neighbor in neighbors:
                to_node = neighbor[0] if isinstance(neighbor, tuple) else neighbor
                edges.append((from_node, to_node))
        return edges
    
    def bfs(self, start):
        if start not in self.adj_list:
            return []
            
        visited = set()
        queue = [start]
        order = []
        visited.add(start)

        while queue:
            node = queue.pop(0)
            order.append(node)
            
            neighbors = self.get_neighbors(node)
            for neighbor in neighbors:
                neighbor_node = neighbor[0] if isinstance(neighbor, tuple) else neighbor
                if neighbor_node not in visited:
                    visited.add(neighbor_node)
                    queue.append(neighbor_node)
        
        return order

    def dfs(self, start):
        if start not in self.adj_list:
            return []

        visited = set()
        stack = [start]
        order = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
                
                neighbors = self.get_neighbors(node)
                sorted_neighbors = sorted([n[0] if isinstance(n, tuple) else n for n in neighbors], reverse=True)
                
                for neighbor_node in sorted_neighbors:
                    if neighbor_node not in visited:
                        stack.append(neighbor_node)
        
        return order
    
if __name__ == '__main__':
    graph = Graph(directed=False)
    
    graph.add_node('Z')
    
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('C', 'E')
    graph.add_edge('D', 'F')
    graph.add_edge('E', 'F')
    graph.add_edge('F', 'Z')
    
    print(graph)
    
    print(f"All Nodes: {graph.get_nodes()}")
    print(f"All Edges: {graph.get_edges()}")
    print(f"Neighbors of 'A': {graph.get_neighbors('A')}")
    
    print(f"Has node 'C': {graph.has_node('C')}")
    print(f"Has node 'X': {graph.has_node('X')}")
    print(f"Has edge 'A'-'B': {graph.has_edge('A', 'B')}")
    print(f"Has edge 'A'-'D': {graph.has_edge('A', 'D')}")
    
    print(f"BFS starting from 'A': {graph.bfs('A')}")
    print(f"DFS starting from 'A': {graph.dfs('A')}")
    
    graph.remove_edge('A', 'B')
    print(f"Has edge 'A'-'B' after remove_edge: {graph.has_edge('A', 'B')}")
    
    graph.remove_node('Z')
    print(f"Has node 'Z' after remove_node: {graph.has_node('Z')}")
    print(f"All Nodes after removals: {graph.get_nodes()}")
    
    weighted_graph = Graph(directed=True)
    weighted_graph.add_node('X')
    weighted_graph.add_edge('X', 'Y', weight=15)
    weighted_graph.add_edge('X', 'Z', weight=25)
    
    print(weighted_graph)
    print(f"Weighted Edges: {weighted_graph.get_edges()}")