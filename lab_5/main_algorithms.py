import random

class Graph:
    # Graph class to manage vertices and edges
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = {}  # Dictionary to store graph

    # Method to add an edge between two vertices with a given weight
    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = {}
        self.graph[u][v] = w

class Algorithms:
    # Kruskal's algorithm to find the Minimum Spanning Tree (MST) of a graph
    def kruskal(self, graph):
        result = []  # To store the resultant MST
        graph_edges = self.get_edges(graph)  # Retrieve all edges from the graph
        graph_edges.sort(key=lambda x: x[2])  # Sort edges by weight

        parent = {node: node for node in graph}  # Initialize parent for union-find

        # Process smallest edges and check for cycle formation
        for u, v, w in graph_edges:
            if self.find(parent, u) != self.find(parent, v):
                result.append([u, v, w])
                self.union(parent, u, v)

        return result

    # Prim's algorithm to find MST of a connected, undirected graph with weighted edges
    def prim(self, graph):
        mst = []  # To store the resultant MST
        keys = {node: float('inf') for node in graph}  # Priority queue for vertices
        keys[0] = 0  # Start from vertex 0
        parent = {node: None for node in graph}  # Parent dictionary to store MST

        # While there are vertices not yet included in MST
        while keys:
            u = min(keys, key=keys.get)  # Vertex with the smallest key value
            del keys[u]  # Remove vertex from queue

            # For each adjacent vertex v, check if it should be updated
            for v in graph[u]:
                if v in keys and graph[u][v] < keys[v]:
                    keys[v] = graph[u][v]
                    parent[v] = u

        # Create MST list from parent dictionary
        for v, p in parent.items():
            if p is not None:
                mst.append([p, v, graph[p][v]])

        return mst

    # Helper method to get all edges from a graph in form (u, v, weight)
    def get_edges(self, graph):
        edges = []
        for u in graph:
            for v, w in graph[u].items():
                edges.append((u, v, w))
        return edges

    # Helper method for union operation in union-find
    def union(self, parent, u, v):
        p1 = self.find(parent, u)
        p2 = self.find(parent, v)
        parent[p2] = p1

    # Helper method for find operation in union-find
    def find(self, parent, node):
        if parent[node] != node:
            parent[node] = self.find(parent, parent[node])
        return parent[node]

    # Method to generate a dense graph with random weights
    def generate_dense_graph(self, nodes):
        graph = {i: {j: random.randint(1, 10) for j in range(nodes) if j != i} for i in range(nodes)}
        return graph

    # Method to generate a sparse graph with a given number of edges
    def generate_sparse_graph(self, nodes, edges):
        graph = {i: {} for i in range(nodes)}
        for _ in range(edges):
            node1, node2 = random.sample(range(nodes), 2)
            weight = random.randint(1, 10)
            graph[node1][node2] = weight
            graph[node2][node1] = weight  # Ensure the graph is undirected
        return graph
