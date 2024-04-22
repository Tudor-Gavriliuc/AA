import sys
import random

class Algorithms:
    # Implement Dijkstra's algorithm to find the shortest paths from a starting node
    def dijkstra(graph, start):
        # Initialize distances from start to all other nodes as infinite, except for the start node itself
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        visited = set()

        # Iterate until all nodes are visited
        while len(visited) < len(graph):
            # Select the unvisited node with the smallest distance
            current_node = min((node for node in graph if node not in visited), key=lambda x: distances[x])
            visited.add(current_node)

            # Update the distance for each adjacent node
            for neighbor, weight in graph[current_node].items():
                new_distance = distances[current_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

        return distances

    # Implement Floyd-Warshall algorithm to find shortest paths between all pairs of nodes
    def floyd_warshall(graph):
        # Initialize distance matrix from every node to every other node
        dist = {i: {j: float('inf') for j in graph} for i in graph}
        for i in graph:
            dist[i][i] = 0  # Distance to itself is zero
            for j, w in graph[i].items():
                dist[i][j] = w  # Distance to direct neighbors

        # Update distances across every pair of nodes through another node
        for k in graph:
            for i in graph:
                for j in graph:
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        return dist

    # Generate a sparse graph with a specified number of nodes and edges
    def generate_sparse_graph(nodes, edges):
        graph = {i: {} for i in range(nodes)}
        for _ in range(edges):
            node1, node2 = random.sample(range(nodes), 2)
            weight = random.randint(1, 10)
            graph[node1][node2] = weight
            graph[node2][node1] = weight  # Ensure the graph is undirected
        return graph

    # Generate a dense graph with all possible edges between nodes, with random weights
    def generate_dense_graph(nodes):
        graph = {i: {j: random.randint(1, 10) for j in range(nodes) if j != i} for i in range(nodes)}
        return graph