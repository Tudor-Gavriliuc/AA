from collections import defaultdict, deque


class GraphDFS:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):

        visited.add(v)

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self, v):

        visited = set()
        self.DFSUtil(v, visited)


class GraphBFS:
    def __init__(self):
        # Initialize an empty adjacency list using defaultdict
        self.adjList = defaultdict(list)

    def addEdge(self, u, v):
        # Add an undirected edge between vertices u and v
        self.adjList[u].append(v)
        self.adjList[v].append(u)

    def show(self, adjList):
        # Display the adjacency list (not used in BFS algorithm)
        for key, value in adjList.items():
            print(key, "   ", value, "\n")

    def bfs(self, startNode):
        # Initialize a queue for BFS traversal
        queue = deque()
        # Find the maximum node in the graph
        max_node = max(self.adjList.keys(), default=-1)
        # Initialize a boolean array to keep track of visited nodes
        visited = [False] * (max_node + 1)

        # Mark the startNode as visited and enqueue it
        visited[startNode] = True
        queue.append(startNode)

        # Perform BFS traversal
        while queue:
            # Dequeue a node from the queue
            currentNode = queue.popleft()

            # Iterate through all neighbors of the current node
            for neighbor in self.adjList[currentNode]:
                # Check if the neighbor has not been visited
                if not visited[neighbor]:
                    # Mark the neighbor as visited and enqueue it
                    visited[neighbor] = True
                    queue.append(neighbor)

graph = GraphBFS()

# Add some edges to the graph
graph.addEdge(1, 2)
graph.addEdge(1, 3)
graph.addEdge(2, 4)

# Call the show function to display the adjacency list
graph.show(graph.adjList)